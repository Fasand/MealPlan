from django.contrib import admin

from .models import (Category, Tag, Nutrition, Unit, Ingredient, Inventory,
                     Recipe, RecipeIngredient)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 5


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "servings", "get_serving_nutrition")
    fieldsets = [
        ("Information", {"fields": ["name", "servings", "prep_time",
                                    "cook_time", "tags"]}),
        ("Directions",  {"fields": ["directions"]}),
    ]
    inlines = [RecipeIngredientInline]


class UnitAdmin(admin.ModelAdmin):
    list_display = ("unit_type", "name", "shorthand", "is_ingredient_unit")


class IngredientUnitsInline(admin.StackedInline):
    model = Unit
    extra = 0


class IngredientNutritionInline(admin.StackedInline):
    model = Nutrition


class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientUnitsInline, IngredientNutritionInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Inventory)
