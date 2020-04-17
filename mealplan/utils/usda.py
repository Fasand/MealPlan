import os
import pandas as pd
from django.conf import settings


PROJECT_DIR = os.path.split(settings.BASE_DIR)[0]
USDA_DIR = os.path.join(PROJECT_DIR, 'usda_sr_legacy')
USDA_FOOD_DIR = os.path.join(USDA_DIR, 'sr_legacy_food')
USDA_SUPPORT_DIR = os.path.join(USDA_DIR, 'supporting_data')

# Food
FOOD_NUTRIENT = os.path.join(USDA_FOOD_DIR, 'food_nutrient.csv')
FOOD_PORTION = os.path.join(USDA_FOOD_DIR, 'food_portion.csv')
FOOD = os.path.join(USDA_FOOD_DIR, 'food.csv')
# Support
FOOD_CATEGORY = os.path.join(USDA_SUPPORT_DIR, 'food_category.csv')
NUTRIENT = os.path.join(USDA_SUPPORT_DIR, 'nutrient.csv')

# Useless weight units
WEIGHT_UNITS = ['g', 'gram', 'oz', 'ounce', 'lb', 'pound']
# From unit key to ml
VOLUME_CONVERSION = {
    'milliliter': 1.0,
    'ml': 1.0,
    'l': 1000.0,
    'liter': 1000.0,
    'tsp': 4.92892159,
    'teaspoon': 4.92892159,
    'tbsp': 14.7867648,
    'tablespoon': 14.7867648,
    'fl oz': 29.5735296,
    'fluid ounce': 29.5735296,
    'cup': 236.588237,
    'pint': 473.176473,
    'quart': 946.352946,
    'gallon': 3785.41178,
    'cubic inch': 16.387064,
}


def import_categories():
    df = pd.read_csv(FOOD_CATEGORY,
                     usecols=['id', 'description'])
    for category in df.iloc:
        usda_id = category['id']
        title = category['description']
        print(usda_id, title)
        # TODO: create IngredientCategory


def import_ingredients():
    df = pd.read_csv(FOOD,
                     usecols=['fdc_id', 'description', 'food_category_id'])
    for ingredient in df.iloc:
        usda_fdc_id = ingredient['fdc_id']
        title = ingredient['description']
        category_usda_id = ingredient['food_category_id']
        # TODO: find category by usda_id, must exist! (if not, throw error)
        # TODO: create Ingredient


def import_nutrients():
    df = pd.read_csv(FOOD_NUTRIENT,
                     usecols=['fdc_id', 'nutrient_id', 'amount'])
    for nutrient in df.iloc:
        usda_fdc_id = nutrient['fdc_id']
        nutrient_id = nutrient['nutrient_id']
        amount = nutrient['amount']


def import_portions():
    df = pd.read_csv(FOOD_PORTION,
                     usecols=['id', 'fdc_id', 'amount',
                              'modifier', 'gram_weight'])
    # Drop base weight units: oz, lb
    df.drop(df.loc[df['modifier'].isin(WEIGHT_UNITS)].index, inplace=True)
    # Drop amount=0 rows, mostly useless
    df.drop(df.loc[df['amount'] == 0].index, inplace=True)
    # Iterate through ingredients
    for fdc_id in df['fdc_id'].unique():  # count 6659
        # TODO: get the ingredient using fdc_id
        portions = df[df['fdc_id'] == fdc_id]
        # Single out volume-based units
        volume_selector = portions['modifier'].isin(VOLUME_CONVERSION.keys())
        volume = portions[volume_selector]
        # If there are any, compute the ingredient's density
        density = None
        if len(volume) > 0:
            # Maximum gram weight, so maximum resolution
            max_volume = volume.iloc[volume['gram_weight'].argmax()]
            multiplier = VOLUME_CONVERSION[max_volume['modifier']]
            volume_in_ml = max_volume['amount'] * multiplier
            # g/ml * 1000 = kg/m^3
            density = (max_volume['gram_weight'] / volume_in_ml) * 1000.0
        # Only import the specific non-volume portion units
        non_volume = portions[~volume_selector]
        for portion in non_volume:
            usda_id = portion['id']
            amount = portion['amount']
            modifier = portion['modifier']
            # Combine amount with modifier if amount is not 1
            if amount != 1:
                title = f"{amount} {modifier}"  # e.g. "2 waffles"
            else:
                title = modifier
            amount_in_base = portion['gram_weight']
            # TODO: create IngredientUnit (unit_type=weight, unit_system=metric)
