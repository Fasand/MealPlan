from django.contrib import admin

from core.admin import BaseModelAdmin
from nutrition.admin import NutritionInline
from .models import (
    Ingredient, IngredientCategory, IngredientUnit,
)


@admin.register(Ingredient)
class IngredientAdmin(BaseModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'category', 'density', 'usda_fdc_id', 'user')
    inlines = [
        NutritionInline,
    ]


@admin.register(IngredientCategory)
class IngredientCategoryAdmin(BaseModelAdmin):
    list_display = ('title', 'description', 'usda_id')


@admin.register(IngredientUnit)
class IngredientUnitAdmin(BaseModelAdmin):
    search_fields = ('title', 'shorthand')
    list_display = (
        'title', 'shorthand', 'unit_type', 'unit_system', 'usda_id',
        'amount_in_base', 'ingredient'
    )
