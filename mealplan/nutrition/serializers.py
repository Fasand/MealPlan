from rest_framework import serializers

from .models import Nutrition


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        # TODO: only send filled in or only essential or sth
        exclude = ('ingredient', 'active')
