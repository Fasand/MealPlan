from rest_framework import serializers

from .models import (Ingredient, IngredientCategory, IngredientUnit)
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
    nutrition = NutritionSerializer(required=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=IngredientCategory.objects.all(), required=False)
    units = IngredientUnitSerializer(many=True)

    def create(self, validated_data):
        ingredient = Ingredient.objects.create(**validated_data)
        # Create an empty nutrition if none supplied
        if validated_data.get('nutrition') is None:
            Nutrition.objects.create(ingredient=ingredient)
        return ingredient

    class Meta:
        model = Ingredient
        fields = (
            'id', 'user', 'title', 'description', 'category', 'tags', 'image',
            'usda_fdc_id', 'density', 'nutrition', 'units',
        )
