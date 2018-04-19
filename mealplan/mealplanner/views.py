from django.shortcuts import render
from django.http import HttpResponse

# Eventually, I would like to convert some of these either to Django premade
# views or something handy of my own creation.
# For now, let's stick with the basics.

def index(request):
    context = {}
    return render(request, "mealplanner/index.html", context)

def ingredients(request):
    context = {}
    return render(request, "mealplanner/ingredients.html", context)

def recipes(request):
    context = {}
    return render(request, "mealplanner/recipes.html", context)

def inventory(request):
    context = {}
    return render(request, "mealplanner/inventory.html", context)

def planner(request):
    context = {}
    return render(request, "mealplanner/planner.html", context)