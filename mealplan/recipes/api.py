from rest_framework import viewsets

from .serializers import (RecipeSerializer)


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        # Return only the user's ingredients
        return self.request.user.recipes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
