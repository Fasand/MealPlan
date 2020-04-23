from rest_framework import serializers

from .models import (Ingredient, IngredientCategory, IngredientUnit)
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
    nutrition = NutritionSerializer()
    category = IngredientCategorySerializer()
    units = serializers.ListField(IngredientUnitSerializer)

    class Meta:
        model = Ingredient
        fields = (
            'user', 'title', 'description', 'category', 'tags', 'image',
            'usda_fdc_id', 'density', 'nutrition', 'units',
        )
