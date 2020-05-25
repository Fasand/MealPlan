from rest_framework import serializers

from core.serializers import TagField
from ingredients.serializers import (IngredientSerializer,
                                     IngredientUnitSerializer)
from ingredients.models import IngredientUnit
from .models import (
    Recipe, RecipeSection, SectionIngredient, SectionDirection,
    PreparationMethod
)


class IngredientPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return self.context['request'].user.ingredients


class SectionIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientPrimaryKeyRelatedField()
    unit = serializers.PrimaryKeyRelatedField(
        queryset=IngredientUnit.objects.filter(ingredient=None)
    )

    class Meta:
        model = SectionIngredient
        exclude = ('section',)


class SectionDirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionDirection
        exclude = ('section',)


class RecipeSectionSerializer(serializers.ModelSerializer):
    ingredients = SectionIngredientSerializer(many=True)
    directions = SectionDirectionSerializer(many=True)

    class Meta:
        model = RecipeSection
        exclude = ('recipe',)


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagField(required=False)
    sections = RecipeSectionSerializer(many=True)

    def create(self, validated_data):
        # Deal with sections separately
        sections = validated_data.pop('sections', [])
        # Create recipe
        recipe = Recipe.objects.create(**validated_data)
        # Create each section and its ingredients+directions
        for section in sections:
            section_ingredients = section.pop('ingredients', [])
            section_directions = section.pop('directions', [])
            recipe_section = RecipeSection.objects.create(
                recipe=recipe, **section)

            for section_ingredient in section_ingredients:
                SectionIngredient.objects.create(
                    section=recipe_section, **section_ingredient)
            for section_direction in section_directions:
                SectionDirection.objects.create(
                    section=recipe_section, **section_direction)

        return recipe

    class Meta:
        model = Recipe
        fields = (
            'id', 'user', 'title', 'description', 'tags', 'image',
            'sources', 'servings', 'difficulty', 'notes', 'scaled_to',
            'sections',
        )
