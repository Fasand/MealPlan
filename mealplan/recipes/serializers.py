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
    id = serializers.IntegerField(required=False)
    ingredient = IngredientPrimaryKeyRelatedField()
    unit = serializers.PrimaryKeyRelatedField(
        queryset=IngredientUnit.objects.filter(ingredient=None)
    )

    class Meta:
        model = SectionIngredient
        exclude = ('section',)


class SectionDirectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = SectionDirection
        exclude = ('section',)


class RecipeSectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
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
        for s in sections:
            section_ingredients = s.pop('ingredients', [])
            section_directions = s.pop('directions', [])
            section = RecipeSection.objects.create(
                recipe=recipe, **s)

            for si in section_ingredients:
                SectionIngredient.objects.create(
                    section=section, **si)
            for sd in section_directions:
                SectionDirection.objects.create(
                    section=section, **sd)

        return recipe

    def update(self, recipe, validated_data):
        # Deal with sections separately
        sections = validated_data.pop('sections', [])
        # Update recipe
        for attr, val in validated_data.items():
            setattr(recipe, attr, val)
        recipe.save()
        # Update or create each section and its ingredients+directions
        # Keep track of updated sections (some might be deleted)
        new_sections = set()
        for s in sections:
            section_ingredients = s.pop('ingredients', [])
            section_directions = s.pop('directions', [])
            section_id = s.pop('id', None)

            # Might be a new section or a bad section id
            try:
                section = recipe.sections.get(pk=section_id)
                for attr, val in s.items():
                    setattr(section, attr, val)
                section.save()
            except RecipeSection.DoesNotExist:
                section = recipe.sections.create(**s)
            new_sections.add(section.pk)

            # Similar with section ingredients and directions
            # Keep track of updated ingredients and directions
            new_ingredients = set()
            for si in section_ingredients:
                ingredient_id = si.pop('id', None)
                try:
                    ingredient = section.ingredients.get(pk=ingredient_id)
                    for attr, val in si.items():
                        setattr(ingredient, attr, val)
                    ingredient.save()
                except SectionIngredient.DoesNotExist:
                    ingredient = section.ingredients.create(**si)
                new_ingredients.add(ingredient.pk)

            new_directions = set()
            for sd in section_directions:
                direction_id = sd.pop('id', None)
                try:
                    direction = section.directions.get(pk=direction_id)
                    for attr, val in sd.items():
                        setattr(direction, attr, val)
                    direction.save()
                except SectionDirection.DoesNotExist:
                    direction = section.directions.create(**sd)
                new_directions.add(direction.pk)

            # Delete removed ingredients
            old_ingredients = set(
                section.ingredients.values_list('pk', flat=True))
            section.ingredients.filter(
                pk__in=old_ingredients-new_ingredients).delete()
            # Delete removed directions
            old_directions = set(
                section.directions.values_list('pk', flat=True))
            section.directions.filter(
                pk__in=old_directions-new_directions).delete()

        # Delete removed sections
        old_sections = set(recipe.sections.values_list('pk', flat=True))
        recipe.sections.filter(pk__in=old_sections-new_sections).delete()

        return recipe

    class Meta:
        model = Recipe
        fields = (
            'id', 'user', 'title', 'description', 'tags', 'image',
            'sources', 'servings', 'difficulty', 'notes', 'scaled_to',
            'sections',
        )
