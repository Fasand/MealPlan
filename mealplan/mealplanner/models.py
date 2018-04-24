from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Nutrition(models.Model):
    # More fields can be added in the future,
    calories = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    # ...

class Unit(models.Model):
    # Unit type: weight-based or volume-based (G or ML)
    unit_type = models.CharField(
        max_length=2,
        choices=(
            ("g", "g (weight)"),
            ("ml", "ml (volume)"),
        ),
        default="g"
    )
    # How many {unit_type} does this unit equate to
    value = models.FloatField()
    # Readable name, e.g. kilograms, rashers (bacon)
    name = models.CharField(max_length=50)
    # Shorthand name, e.g. kg, rashers
    shorthand = models.CharField(max_length=20)
    # Ingredient the unit belongs to. If null, it can be used for any ingredient (e.g. kg, oz)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, null=True)

class Ingredient(models.Model):
    # Name of the ingredient, can be rather long if needed
    name = models.CharField(max_length=100)
    # Category: e.g. vegetables, spices, etc.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # Tags: e.g. mexican, spicy
    tags = models.ManyToManyField(Tag)
    # Unit type: weight-based or volume-based (G or ML)
    unit_type = models.CharField(
        max_length=2,
        choices=(
            ("g", "g (weight)"),
            ("ml", "ml (volume)"),
        ),
        default="g"
    )
    # Which unit should be provided by default when selecting this ingredient
    preferred_unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    # Nutrition per 100 g/ml: there will be many possible fields so create a separate model
    nutrition = models.OneToOneField(Nutrition, on_delete=models.PROTECT)
    # Price per 100 g/ml
    price = models.FloatField(blank=True, default=0.0)
    # Description: either text description or a generated recipe (feature idea)
    description = models.TextField(blank=True, default="")

class Inventory(models.Model):
    # Ingredient which is in your inventory
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # Quantity of that ingredient that you have (in unit_type)
    quantity = models.FloatField()

class Recipe(models.Model):
    # Name of the recipe
    name = models.CharField(max_length=100)
    # Number of servings the recipe yields
    servings = models.PositiveSmallIntegerField()
    # Preparation time (in minutes)
    prep_time = models.DurationField()
    # Cooking time (in minutes)
    cook_time = models.DurationField()
    # Tags: e.g. mexican, spicy
    tags = models.ManyToManyField(Tag)
    # Ingredients this recipe composes of
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
    )
    # Directions: can be text for now, maybe change to JSON later
    directions = models.TextField()

class RecipeIngredient(models.Model):
    # The two foreign keys this is related to
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # Unit used for display. If null, use base unit_type instead
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    # Quantity of the ingredient in terms of its base unit_type
    quantity = models.FloatField()
