from rest_framework import viewsets

from .models import (IngredientCategory, IngredientUnit)
from .serializers import (
    IngredientSerializer, IngredientCategorySerializer, IngredientUnitSerializer)

# TODO BIG: create a BaseModelViewSet which updates created_by, modified_by


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        # Return only the user's ingredients
        return self.request.user.ingredients.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IngredientCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientCategorySerializer
    queryset = IngredientCategory.objects.all()


class IngredientUnitViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientUnitSerializer
    queryset = IngredientUnit.objects.filter(ingredient=None)
