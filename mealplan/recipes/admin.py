from django.contrib import admin

from core.admin import (BaseModelAdmin, BaseModelTabularInline)
from .models import (
    Recipe, RecipeSection, SectionIngredient, SectionDirection,
    PreparationMethod
)


class RecipeSectionInline(BaseModelTabularInline):
    model = RecipeSection
    fields = (
        'title',
    )


@admin.register(Recipe)
class RecipeAdmin(BaseModelAdmin):
    inlines = [
        RecipeSectionInline,
    ]


@admin.register(PreparationMethod)
class PreparationMethodAdmin(BaseModelAdmin):
    list_display = ('title', 'description', 'metric_size', 'imperial_size')
