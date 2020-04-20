from django.contrib import admin

from core.admin import BaseModelStackedInline
from .models import Nutrition


class NutritionInline(BaseModelStackedInline):
    model = Nutrition

    def has_delete_permission(self, request, obj=None):
        """ Don't allow deletion under any circumstances """
        return False
