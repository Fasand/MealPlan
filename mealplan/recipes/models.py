from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from private_storage.fields import PrivateFileField

from core.models import BaseModel, OrderedBaseModel
from core.fields import PrivateImageField
from core.constants import (ALLOWED_IMAGE_MIME_TYPES, MAX_IMAGE_FILE_SIZE)
from . import constants


def recipe_image_path(instance, filename):
    return f"recipe/{instance.pk}/{filename}"


class Recipe(BaseModel):
    # If None, it is public, otherwise private to the user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='recipes',
                             related_query_name='recipe',
                             null=True, blank=True)
    title = models.CharField(_('title'), max_length=128)
    description = models.TextField(_('description'), blank=True)
    tags = models.TextField(_('tags'), blank=True)
    image = PrivateImageField(_('image'),
                              upload_to=recipe_image_path,
                              null=True, blank=True)
    sources = models.TextField(_('sources'), blank=True)
    servings = models.FloatField(_('servings'), null=True, blank=True)
    difficulty = models.IntegerField(_('difficulty'),
                                     choices=constants.DIFFICULTIES,
                                     null=True, blank=True)
    notes = models.TextField(_('notes'), blank=True)
    # In grams what corresponds to 100%
    scaled_to = models.FloatField(_('scaled to'), null=True, blank=True)

    def __str__(self):
        return self.title


class RecipeSection(OrderedBaseModel):
    recipe = models.ForeignKey('recipes.Recipe',
                               on_delete=models.CASCADE,
                               related_name='sections',
                               related_query_name='section')
    title = models.CharField(_('title'), max_length=128, blank=True)

    def __str__(self):
        return f"{self.recipe} | {self.title}"


class SectionIngredient(OrderedBaseModel):
    section = models.ForeignKey('recipes.RecipeSection',
                                on_delete=models.CASCADE,
                                related_name='ingredients',
                                related_query_name='ingredient')
    ingredient = models.ForeignKey('ingredients.Ingredient',
                                   on_delete=models.PROTECT,  # TODO
                                   related_name='in_recipes',
                                   related_query_name='in_recipe')
    # Suggestions given from PreparationMethod
    preparation_method = models.CharField(_('preparation method'),
                                          max_length=64,
                                          blank=True)
    amount = models.FloatField(_('amount'))
    # TODO: Should be recalculated to a different unit on delete (signal)
    # https://stackoverflow.com/questions/36571834/django-pass-self-to-models-set-on-delete
    # TODO: Can I validate that unit belongs to user or is base?
    unit = models.ForeignKey('ingredients.IngredientUnit',
                             on_delete=models.PROTECT,  # TODO
                             related_name='section_ingredients',
                             related_query_name='section_ingredient')
    optional = models.BooleanField(_('optional'), default=False)

    def __str__(self):
        return f"{self.ingredient}, {self.amount} {self.unit}"

# TODO: implement SectionRecipe (so that recipes can act as ingredients)


def section_direction_image_path(instance, filename):
    return (f"recipe/{instance.section.recipe.pk}/"
            f"directions/{instance.pk}/{filename}")


class SectionDirection(OrderedBaseModel):
    section = models.ForeignKey('recipes.RecipeSection',
                                on_delete=models.CASCADE,
                                related_name='directions',
                                related_query_name='direction')
    description = models.TextField(_('description'))
    duration = models.DurationField(_('duration'), null=True, blank=True)
    duration_type = models.CharField(_('duration type'),
                                     max_length=16,
                                     choices=constants.DURATION_TYPES,
                                     blank=True)
    image = PrivateImageField(_('image'),
                              upload_to=section_direction_image_path,
                              null=True, blank=True)
    optional = models.BooleanField(_('optional'), default=False)

    def __str__(self):
        return f"{self.description}"

# TODO: implement IngredientSubstitution
# TODO: implement DirectionSubstitution
# TODO: implement RecipeVariation


class PreparationMethod(BaseModel):
    title = models.CharField(_('title'), max_length=64)
    description = models.TextField(_('description'), blank=True)
    metric_size = models.CharField(
        _('metric size'), max_length=64, blank=True)
    imperial_size = models.CharField(
        _('imperial size'), max_length=64, blank=True)

    def __str__(self):
        return self.title
