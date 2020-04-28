from rest_framework import routers

from .api import (RecipeViewSet)

router = routers.SimpleRouter()
router.register('recipes',
                RecipeViewSet,
                basename='recipes')

urlpatterns = router.urls
