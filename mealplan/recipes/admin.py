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
    show_change_link = True


@admin.register(Recipe)
class RecipeAdmin(BaseModelAdmin):
    inlines = [
        RecipeSectionInline,
    ]


class SectionIngredientInline(BaseModelTabularInline):
    model = SectionIngredient
    autocomplete_fields = ('ingredient', 'unit')


class SectionDirectionInline(BaseModelTabularInline):
    model = SectionDirection


@admin.register(RecipeSection)
class RecipeSectionAdmin(BaseModelAdmin):
    fields = ('title',)
    inlines = [
        SectionIngredientInline,
        SectionDirectionInline,
    ]
    list_display = ('recipe', 'title')


@admin.register(PreparationMethod)
class PreparationMethodAdmin(BaseModelAdmin):
    list_display = ('title', 'description', 'metric_size', 'imperial_size')
