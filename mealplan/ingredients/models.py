from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Ingredient(BaseModel):
    pass

    class Meta():
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        ordering = ('',)


class IngredientCategory(BaseModel):
    pass

    class Meta():
        verbose_name = _('Ingredient Category')
        verbose_name_plural = _('Ingredient Categories')
        ordering = ('',)


class IngredientUnit(BaseModel):
    pass

    class Meta():
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ('',)
