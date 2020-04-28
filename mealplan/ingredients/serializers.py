from rest_framework import serializers

from .models import (Ingredient, IngredientCategory, IngredientUnit)
from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer


class TagField(serializers.Field):
    """
    Tags are converted between a list and a comma-joined string
    """

    def to_representation(self, value):
        ''' data: comma-joined string or the empty string '''
        if type(value) != str:
            raise serializers.ValidationError("Tags must be saved as strings")
        if value and len(value) > 0:
            return value.split(',')
        else:
            return None

    def to_internal_value(self, data):
        ''' data: list(str) or comma-joined string '''
        if type(data) == str:
            return data
        if type(data) == list:
            return [x.strip() for x in data].join(",")
        raise serializers.ValidationError("Tags must be sent as a list")


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
    tags = TagField()

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
