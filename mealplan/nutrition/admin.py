from django.contrib import admin

from core.admin import BaseModelStackedInline
from .models import Nutrition


class NutritionInline(BaseModelStackedInline):
    model = Nutrition
