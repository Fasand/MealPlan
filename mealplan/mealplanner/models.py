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
    #unit_aliases
    
    #preferred_unit

    # Nutrition per 100 g/ml: there will be many possible fields so create a separate model
    nutrition = models.OneToOneField(Nutrition, on_delete=models.PROTECT)
    # Price per 100 g/ml
    price = models.FloatField(blank=True, default=0.0)
    # Description: either text description or a generated recipe (feature idea)
    description = models.TextField(blank=True, default="")
