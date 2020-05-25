from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import (RecipeSerializer)
from .constants import DURATION_TYPES


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        # Return only the user's ingredients
        return self.request.user.recipes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False)
    def duration_types(self, request):
        return Response(DURATION_TYPES)
