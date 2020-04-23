from rest_framework import routers

from .api import (IngredientViewSet, IngredientCategoryViewSet)

router = routers.SimpleRouter()
router.register('ingredients',
                IngredientViewSet,
                basename='ingredients')
router.register('ingredient-categories',
                IngredientCategoryViewSet,
                basename='ingredient-categories')

urlpatterns = router.urls
