from rest_framework import serializers

from .models import (
    Recipe, RecipeSection, SectionIngredient, SectionDirection,
    PreparationMethod
)
from core.serializers import TagField


class ScalingIngredientField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        print("SCALING INGREDIENT", self, super().get_queryset())
        return super().get_queryset()


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagField()
    scaling_ingredient = ScalingIngredientField()

    # TODO
    # def create(self, validated_data):
    #     ingredient = Ingredient.objects.create(**validated_data)
    #     # Create an empty nutrition if none supplied
    #     if validated_data.get('nutrition') is None:
    #         Nutrition.objects.create(ingredient=ingredient)
    #     return ingredient

    class Meta:
        model = Recipe
        fields = (
            'id', 'user', 'title', 'description', 'tags', 'image',
            'sources', 'servings', 'difficulty', 'notes', 'scaling_ingredient',
        )
