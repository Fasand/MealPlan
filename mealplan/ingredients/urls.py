from rest_framework import routers

from .api import (IngredientViewSet,
                  IngredientCategoryViewSet,
                  IngredientUnitViewSet)

router = routers.SimpleRouter()
router.register('ingredients',
                IngredientViewSet,
                basename='ingredients')
router.register('ingredient-categories',
                IngredientCategoryViewSet,
                basename='ingredient-categories')
router.register('ingredient-units',
                IngredientUnitViewSet,
                basename='ingredient-units')

urlpatterns = router.urls
