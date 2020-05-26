from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from private_storage.fields import PrivateFileField

from core.models import BaseModel
from core.fields import PrivateImageField
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
                             max_length=160)
    description = models.TextField(_('description'),
                                   blank=True)
    category = models.ForeignKey('ingredients.IngredientCategory',
                                 on_delete=models.SET_NULL,
                                 related_name='ingredients',
                                 related_query_name='ingredient',
                                 null=True, blank=True)
    tags = models.TextField(_('tags'),
                            blank=True)
    image = PrivateImageField(_('image'),
                              upload_to=ingredient_image_path,
                              null=True, blank=True)
    usda_fdc_id = models.PositiveIntegerField(_('usda fdc id'),
                                              null=True, blank=True)
    density = models.FloatField(_('density'),
                                null=True, blank=True)

    # nutrition is added through a OneToOne relationship from Nutrition

    def load_from_usda(self, usda):
        if usda.usda_fdc_id == None:
            raise Exception("Not a USDA ingredient")
        # Replace most fields with those in USDA
        self.category = usda.category
        self.density = usda.density
        self.usda_fdc_id = usda.usda_fdc_id
        # Replace nutrition completely by cloning target nutrition
        if hasattr(self, "nutrition"):
            self.nutrition.delete()
        nutrition = usda.nutrition
        nutrition.pk = None
        nutrition.id = None
        nutrition.ingredient = self
        nutrition.save()
        # Copy custom units
        self.units.set(usda.units.all())
        # Save instance
        self.save()

    def __str__(self):
        return f"{self.title}"

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
    image = PrivateImageField(_('image'),
                              upload_to=ingredient_category_image_path,
                              null=True, blank=True)
    usda_id = models.PositiveIntegerField(_('usda id'),
                                          null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

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
                                 max_length=16,
                                 blank=True)
    unit_type = models.CharField(_('unit type'),
                                 max_length=16,
                                 choices=constants.UNIT_TYPES)
    # Custom means it's a user-created unit, or e.g. USDA units
    unit_system = models.CharField(_('unit system'),
                                   max_length=16,
                                   choices=constants.UNIT_SYSTEMS,
                                   default=constants.UNIT_SYSTEM_CUSTOM)
    usda_id = models.PositiveIntegerField(_('usda id'),
                                          null=True, blank=True)
    # Base is "gram" for unit_type=weight, "mililiter" for unit_type=volume
    amount_in_base = models.FloatField(_('amount in base unit'))

    def __str__(self):
        return f"{self.title}" + (" (I)" if self.ingredient else '')

    class Meta():
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ('ingredient', 'unit_system', 'unit_type', 'amount_in_base')
