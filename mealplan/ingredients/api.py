from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import (Ingredient, IngredientCategory, IngredientUnit)
from .serializers import (
    IngredientSerializer, IngredientCategorySerializer, IngredientUnitSerializer, IngredientSearchSerializer)

# TODO BIG: create a BaseModelViewSet which updates created_by, modified_by


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        # Return only the user's ingredients
        return self.request.user.ingredients.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["GET", "POST"], detail=False)
    def usda(self, request):
        # Search USDA ingredients
        if request.method == "GET":
            MAX_RESULTS = 30
            q = request.query_params.get('q', "")
            if len(q) >= 3:
                return Response(IngredientSearchSerializer(
                    Ingredient.objects.exclude(usda_fdc_id=None).filter(
                        user=None, title__search=q)[:MAX_RESULTS],
                    many=True
                ).data)
            return Response([])
        # Load data from USDA
        elif request.method == "POST":
            ingredient_id = request.data.get('ingredient', None)
            usda_id = request.data.get('usdaIngredient', None)
            if ingredient_id and usda_id:
                try:
                    ingredient = request.user.ingredients.get(pk=ingredient_id)
                    usda = Ingredient.objects.get(pk=usda_id)
                    ingredient.load_from_usda(usda)
                    return Response(IngredientSerializer(ingredient).data)
                except Ingredient.DoesNotExist:
                    raise ValidationError(
                        "Ingredient doesn't exist or belong to you")
                except:
                    raise ValidationError("An error occured")
            else:
                raise ValidationError("Ingredients not selected correctly")


class IngredientCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientCategorySerializer
    queryset = IngredientCategory.objects.all()


class IngredientUnitViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientUnitSerializer
    queryset = IngredientUnit.objects.filter(ingredient=None)
