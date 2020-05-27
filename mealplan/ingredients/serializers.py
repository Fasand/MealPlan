from rest_framework import serializers

from .models import (Ingredient, IngredientCategory, IngredientUnit)
from core.serializers import TagField
from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer


class IngredientUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientUnit
        fields = '__all__'


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    nutrition = NutritionSerializer(required=False, allow_null=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=IngredientCategory.objects.all(),
        required=False, allow_null=True)
    units = IngredientUnitSerializer(many=True, required=False)
    tags = TagField(required=False)
    density = serializers.FloatField(required=False, allow_null=True)

    def create(self, validated_data):
        nutrition_data = validated_data.pop('nutrition', {})
        # Create ingredient from data
        ingredient = Ingredient.objects.create(**validated_data)
        # Create nutrition from data
        Nutrition.objects.create(ingredient=ingredient, **nutrition_data)
        return ingredient

    def update(self, ingredient, validated_data):
        nutrition_data = validated_data.pop('nutrition', {})
        # Create an empty nutrition if none exists
        if hasattr(ingredient, 'nutrition'):
            nutrition = ingredient.nutrition
        else:
            nutrition = Nutrition.objects.create(ingredient=ingredient)
        # Update ingredient
        for attr, val in validated_data.items():
            setattr(ingredient, attr, val)
        ingredient.save()
        # Update nutrition
        for attr, val in nutrition_data.items():
            setattr(nutrition, attr, val)
        nutrition.save()
        return ingredient

    class Meta:
        model = Ingredient
        fields = (
            'id', 'user', 'title', 'description', 'category', 'tags', 'image',
            'usda_fdc_id', 'density', 'nutrition', 'units',
        )


class IngredientSearchSerializer(IngredientSerializer):
    class Meta(IngredientSerializer.Meta):
        fields = ('id', 'title')
