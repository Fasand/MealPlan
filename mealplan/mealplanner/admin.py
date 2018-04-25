from django.contrib import admin

from .models import Category, Tag, Nutrition, Unit, Ingredient, Inventory, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 5

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Information", {"fields": ["name", "servings", "prep_time", "cook_time", "tags"]}),
        ("Directions",          {"fields": ["directions"]}),
    ]
    inlines = [RecipeIngredientInline]

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Nutrition)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Inventory)
admin.site.register(Recipe, RecipeAdmin)