from django.contrib import admin

from .models import Category, Tag, Nutrition, Unit, Ingredient, Inventory, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 5

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Information", {"fields": ["name", "servings", "prep_time", "cook_time", "tags"]}),
        ("Directions",  {"fields": ["directions"]}),
    ]
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ("unit_type", "name", "shorthand", "is_ingredient_unit")

admin.site.register(Unit, UnitAdmin)

class NutritionInline(admin.StackedInline):
    model = Nutrition

class IngredientAdmin(admin.ModelAdmin):
    inlines = [NutritionInline]

admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Inventory)