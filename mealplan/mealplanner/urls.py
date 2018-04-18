from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingredients/", views.ingredients, name="ingredients"),
    path("recipes/", views.recipes, name="recipes"),
    path("inventory/", views.inventory, name="inventory"),
    path("planner/", views.planner, name="planner"),
]