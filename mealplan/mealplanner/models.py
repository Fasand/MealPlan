from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=50)

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
    #nutrition
    #price
    #description
