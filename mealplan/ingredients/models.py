from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from private_storage.fields import PrivateFileField

from core.models import BaseModel
from core.constants import (ALLOWED_IMAGE_MIME_TYPES, MAX_IMAGE_FILE_SIZE)
from . import constants


def ingredient_image_path(instance, filename):
    return f"ingredient/{instance.pk}/{filename}"


class Ingredient(BaseModel):
    # If None, it is public, otherwise private to the user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='ingredients',
                             related_query_name='ingredient',
                             null=True, blank=True)
    title = models.CharField(_('title'),
                             max_length=128)
    description = models.TextField(_('description'),
                                   blank=True, null=True)
    category = models.ForeignKey('ingredients.IngredientCategory',
                                 on_delete=models.SET_NULL,
                                 related_name='ingredients',
                                 related_query_name='ingredient',
                                 null=True, blank=True)
    tags = models.TextField(_('tags'),
                            blank=True, null=True)
    image = PrivateFileField(_('image'),
                             upload_to=ingredient_image_path,
                             content_types=ALLOWED_IMAGE_MIME_TYPES,
                             max_file_size=MAX_IMAGE_FILE_SIZE)
    usda_fdc_id = models.PositiveIntegerField(_('usda fdc id'),
                                              null=True, blank=True)
    density = models.FloatField(_('density'),
                                null=True, blank=True)

    # nutrition is added through a OneToOne relationship from Nutrition

    class Meta():
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        ordering = ('usda_fdc_id', 'title')


def ingredient_category_image_path(instance, filename):
    return f"ingredient_category/{instance.pk}/{filename}"


class IngredientCategory(BaseModel):
    title = models.CharField(_('title'),
                             max_length=64)
    description = models.CharField(_('description'),
                                   max_length=128,
                                   blank=True)
    image = PrivateFileField(_('image'),
                             upload_to=ingredient_category_image_path,
                             content_types=ALLOWED_IMAGE_MIME_TYPES,
                             max_file_size=MAX_IMAGE_FILE_SIZE)
    usda_id = models.PositiveIntegerField(_('usda id'),
                                          null=True, blank=True)

    class Meta():
        verbose_name = _('Ingredient Category')
        verbose_name_plural = _('Ingredient Categories')
        ordering = ('title',)


class IngredientUnit(BaseModel):
    # If None, it is a base unit, available to all ingredients
    ingredient = models.ForeignKey('ingredients.Ingredient',
                                   on_delete=models.CASCADE,
                                   related_name='units',
                                   related_query_name='unit',
                                   null=True, blank=True)
    title = models.CharField(_('title'),
                             max_length=128)
    shorthand = models.CharField(_('shorthand'),
                                 max_length=16)
    unit_type = models.CharField(_('unit type'),
                                 max_length=16,
                                 choices=constants.UNIT_TYPES)
    # Custom means it's a user-created unit
    unit_system = models.CharField(_('unit system'),
                                   max_length=16,
                                   choices=constants.UNIT_SYSTEMS,
                                   default=constants.UNIT_SYSTEM_CUSTOM)
    usda_id = models.PositiveIntegerField(_('usda id'),
                                          null=True, blank=True)
    # Base is "gram" for unit_type=weight, "mililiter" for unit_type=volume
    amount_in_base = models.FloatField(_('amount in base unit'))

    class Meta():
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ('ingredient', 'unit_system', 'unit_type', 'amount_in_base')
