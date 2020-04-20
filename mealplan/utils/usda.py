import os
import re
import pandas as pd
from django.conf import settings

from ingredients.models import (
    Ingredient, IngredientCategory, IngredientUnit
)
from ingredients import constants as ingredient_constants
from nutrition.models import Nutrition


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


def get_nutrient_variable_name(name):
    ''' Clean up the nutrient name for a variable name '''
    var_name = name.lower().strip()
    # Variables can't start with a number, all numbered are acids
    if var_name[0].isnumeric():
        var_name = 'acid_' + var_name
    # Perform a couple of substitutions
    for regex, sub in [
        (r'[(),+]', ''),    # remove parentheses and commas
        (r'\s+', ' '),      # combine adjacent spaces into one
        (r'[:\-\s/]', '_'),  # replace bad characters with underscores
    ]:
        var_name = re.sub(regex, sub, var_name)
    # Make sure it is now a valid variable name
    if not var_name.isidentifier():
        raise Exception(f"'{var_name}' is not a valid identifier")
    return var_name


def load_nutrient_definitions():
    df = pd.read_csv(FOOD_NUTRIENT)
    nutrients = pd.read_csv(NUTRIENT)
    num_ingredients = len(df['fdc_id'].unique())
    # Compute number of occurences
    nutrients['num'] = [len(df[df['nutrient_id'] == nutrient['id']])
                        for nutrient in nutrients.iloc]
    nutrients['percentage'] = (nutrients['num'] / num_ingredients) * 100.0
    # Generate the variable name used for field definition
    nutrients['var_name'] = [get_nutrient_variable_name(n)
                             for n in nutrients['name']]
    return nutrients


def print_nutrient_fields(sort_by='id', include_null=True):
    nutrients = load_nutrient_definitions()
    # Filter only non-null if specified
    if not include_null:
        nutrients = nutrients[nutrients['percentage'] != 0]
    nutrients.sort_values(sort_by, inplace=True)

    max_unit_len = max(map(len, nutrients['unit_name']))
    max_var_len = max(map(len, nutrients['var_name']))
    field_len = len(" = models.FloatField(")
    comment_len = 2 + 5 + max_unit_len
    definition_len = max_var_len + field_len

    for nutrient in nutrients.iloc:
        nutrient_id = nutrient['id']
        name = nutrient['name']
        unit_name = nutrient['unit_name']
        var_name = nutrient['var_name']

        # Combine into a model field definition
        comment = f"# {nutrient_id} {unit_name}"
        line = (
            f"{(var_name + ' = models.FloatField(').ljust(definition_len)} "
            f"{comment.ljust(comment_len)}\n"
            f"\t_('{name}'), null=True, blank=True)"
        )
        print(line)


def print_nutrient_usage():
    df = pd.read_csv(FOOD_NUTRIENT)
    nutrients = load_nutrient_definitions()
    # Sort by percentage
    nutrients.sort_values('percentage', ascending=False, inplace=True)

    for nutrient in nutrients.iloc:
        num = nutrient['num']
        percentage = nutrient['percentage']
        if percentage == 100:
            sign = 'XXX'
        elif percentage > 80:
            sign = ' * '
        elif percentage > 10:
            sign = ' - '
        else:
            sign = ''
        if num > 0:
            print(f"{sign:^3} ({percentage:>4.1f}) {num:<4} "
                  f"– {nutrient['id']} {nutrient['name']}")
    return nutrients


def import_categories():
    """ Imports all USDA categories, create IngredientCategory """
    df = pd.read_csv(FOOD_CATEGORY,
                     usecols=['id', 'description'])
    categories_created = 0
    for category in df.iloc:
        obj, created = IngredientCategory.objects.get_or_create(
            title=category['description'],
            usda_id=category['id'],
        )
        categories_created += created
    print(f"Ingredient categories imported, total new: {categories_created}")


def import_ingredient_units():
    """ Import all USDA ingredient units after Ingredients have been created """
    df = pd.read_csv(FOOD_PORTION,
                     usecols=['id', 'fdc_id', 'amount',
                              'modifier', 'gram_weight'])
    # Drop base weight units: oz, lb
    df.drop(df.loc[df['modifier'].isin(WEIGHT_UNITS)].index, inplace=True)
    # Drop amount=0 rows, mostly useless
    df.drop(df.loc[df['amount'] == 0].index, inplace=True)
    # Iterate through ingredients
    units_created = 0
    total_ingredients = len(df['fdc_id'].unique())
    for i, fdc_id in enumerate(df['fdc_id'].unique()):  # count 6659
        # Print progress
        if i % 100 == 0:
            print(
                f"Units imported: {i:>5} / {total_ingredients} (ingredients)")
        # Get the Ingredient using fdc_id
        ingredient = Ingredient.objects.get(usda_fdc_id=fdc_id)
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
        for portion in non_volume.iloc:
            usda_id = portion['id']
            amount = portion['amount']
            modifier = portion['modifier']
            # Combine amount with modifier if amount is not 1
            if amount != 1:
                title = f"{amount} {modifier}"  # e.g. "2 waffles"
            else:
                title = modifier
            amount_in_base = portion['gram_weight']
            # Create IngredientUnit
            unit, created = IngredientUnit.objects.get_or_create(
                ingredient=ingredient,
                title=title,
                unit_type=ingredient_constants.UNIT_TYPE_WEIGHT,
                unit_system=ingredient_constants.UNIT_SYSTEM_CUSTOM,
                usda_id=usda_id,
                amount_in_base=amount_in_base,
            )
            units_created += created
        # Save density to the ingredient if it was computed
        if density is not None:
            ingredient.density = density
            ingredient.save()
        print(f"Ingredient units imported, total new: {units_created}")


def import_ingredients():
    """ Import all USDA SR ingredients, create Ingredient """
    # Categories must be imported before importing ingredients
    import_categories()
    # Load nutrition definitions and values
    nutrient_definitions = load_nutrient_definitions()
    food_nutrients = pd.read_csv(
        FOOD_NUTRIENT, usecols=['fdc_id', 'nutrient_id', 'amount'])
    # Load ingredients and iterate through each
    ingredients = pd.read_csv(
        FOOD, usecols=['fdc_id', 'description', 'food_category_id'])
    ingredients_created = 0
    total_ingredients = len(ingredients)
    for i, ingredient in enumerate(ingredients.iloc):
        # Print progress
        if i % 100 == 0:
            print(f"Ingredients imported: {i:>5} / {total_ingredients}")
        usda_fdc_id = ingredient['fdc_id']
        title = ingredient['description']
        # Find category by usda_id, must exist! (if not, throw error)
        category = IngredientCategory.objects.get(
            usda_id=ingredient['food_category_id'])
        # Create Ingredient with the essential information
        ingredient, created = Ingredient.objects.get_or_create(
            usda_fdc_id=usda_fdc_id,
            title=title,
            category=category,
        )
        ingredients_created += created
        # Create Nutrition
        nutrition = Nutrition(ingredient=ingredient)
        # Get nutrients for the specific Ingredient
        nutrients = food_nutrients[food_nutrients['fdc_id'] == usda_fdc_id]
        for nutrient in nutrients.iloc:
            nutrient_id = nutrient['nutrient_id']
            amount = nutrient['amount']
            nutrient_var_name = nutrient_definitions[
                nutrient_definitions['id'] == nutrient_id
            ].iloc[0]['var_name']
            # Set each nutrient
            setattr(nutrition, nutrient_var_name, amount)
        nutrition.save()
    # Ingredient units are imported once all Ingredients have been created
    import_ingredient_units()
    print(f"Ingredients imported, total new: {ingredients_created}")
