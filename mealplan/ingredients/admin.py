from django.contrib import admin

from core.admin import BaseModelAdmin
from .models import (
    Ingredient, IngredientCategory, IngredientUnit,
)


@admin.register(Ingredient)
class IngredientAdmin(BaseModelAdmin):
    pass


@admin.register(IngredientCategory)
class IngredientCategoryAdmin(BaseModelAdmin):
    pass


@admin.register(IngredientUnit)
class IngredientUnitAdmin(BaseModelAdmin):
    pass
