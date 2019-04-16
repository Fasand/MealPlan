from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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
    # Ingredient the unit belongs to. If null, it can be used
    # for any ingredient (e.g. kg, oz)
    belongs_to_ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def is_ingredient_unit(self):
        return self.belongs_to_ingredient is not None
    is_ingredient_unit.boolean = True
    is_ingredient_unit.short_description = "Ingredient unit?"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    # Name of the ingredient, can be rather long if needed
    name = models.CharField(max_length=100)
    # Category: e.g. vegetables, spices, etc.
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    # Tags: e.g. mexican, spicy
    tags = models.ManyToManyField(Tag, blank=True)
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
    preferred_unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # Price per 100 g/ml
    price = models.FloatField(blank=True, default=0.0)
    # Description: either text description or a generated recipe (feature idea)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    # Nutrition per 100 g/ml
    # More fields can be added in the future,
    calories = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    fat_saturated = models.FloatField(null=True, blank=True)
    fat_monounsaturated = models.FloatField(null=True, blank=True)
    fat_polyunsaturated = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    # ...

    # Ingredient to which it belongs
    ingredient = models.OneToOneField(Ingredient,
                                      on_delete=models.CASCADE,
                                      null=True)

    def __str__(self):
        return "{:.0f}kcal, {:.1f}F, {:.1f}C, {:.1f}P".format(
            self.calories,
            self.fat,
            self.carbs,
            self.protein,
        )

    def __add__(self, other):
        if type(other) is not type(self):
            # Needed for sum() to work
            if type(other) is int or type(other) is float:
                return self
            else:
                raise TypeError("Nutrition can be added "
                                "only with other Nutritions")

        # Create a new value dict with added values
        # Don't add ingredient and id -> would throw an error
        tot_vals = {}
        for f in self._meta.get_fields():
            try:
                added = f.value_from_object(self) + f.value_from_object(other)
            except TypeError as e:
                # Fields can be None, pick whichever isn't None
                if f.value_from_object(other) is None:
                    added = f.value_from_object(self)
                else:
                    added = f.value_from_object(other)
            tot_vals[f.name] = added

        # Make sure ID and Ingredient aren't added
        tot_vals["id"] = 0
        tot_vals["ingredient"] = None

        # Create a new Nutrition from the added values
        tot = Nutrition(**tot_vals)
        return tot

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            other = float(other)
        except ValueError:
            raise TypeError("Nutrition can only be multiplied a number")

        # Create a new value dict with added values
        # Don't multiply ingredient and id -> would throw an error
        tot_vals = {}
        for f in self._meta.get_fields():
            try:
                multiplied = f.value_from_object(self) * other
            except TypeError:
                # It's ok if it's None
                multiplied = None
            tot_vals[f.name] = multiplied

        # Make sure ID and Ingredient aren't multiplied
        tot_vals["id"] = 0
        tot_vals["ingredient"] = None

        # Create a new Nutrition from the multiplied values
        tot = Nutrition(**tot_vals)
        return tot

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            other = float(other)
        except ValueError:
            raise TypeError("Nutrition can only be divided a number")

        return self.__mul__(1.0 / other)


class Inventory(models.Model):
    # Ingredient which is in your inventory
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # Quantity of that ingredient that you have (in unit_type)
    quantity = models.FloatField()

    def __str__(self):
        return "{}: {}{}".format(self.ingredient, self.quantity,
                                 self.ingredient.unit_type)


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
    tags = models.ManyToManyField(Tag, blank=True)
    # Ingredients this recipe composes of
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
    )
    # Directions: can be text for now, maybe change to JSON later
    directions = models.TextField()

    def __str__(self):
        return self.name

    def get_recipe_nutrition(self):
        nutritions = []
        for ri in self.recipeingredient_set.all():
            nutritions.append(ri.ingredient.nutrition
                              * (ri.unit.value / 100.0)
                              * ri.quantity)
        return sum(nutritions)

    def get_serving_nutrition(self, servings=None):
        if servings is None:
            servings = float(self.servings)
        return self.get_recipe_nutrition() / servings

    get_serving_nutrition.short_description = "Nutrition per serving"


class RecipeIngredient(models.Model):
    # The two foreign keys this is related to
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # Unit used for display. If null, use base unit_type instead
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    # Quantity of the ingredient in terms of the unit specified
    quantity = models.FloatField()

    def __str__(self):
        return "{} - {}: {:.1f} {}".format(
            self.recipe.name, self.ingredient.name,
            self.quantity, self.unit.shorthand)
