from django.shortcuts import render
from django.http import HttpResponse

# Eventually, I would like to convert some of these either to Django premade
# views or something handy of my own creation.
# For now, let's stick with the basics.

def index(request):
    context = {}
    return render(request, "mealplanner/index.html", context)

def ingredients(request):
    return HttpResponse("This page will contain the user's ingredients.")

def recipes(request):
    return HttpResponse("This page will contain the user's recipes.")

def inventory(request):
    return HttpResponse("This page will contain the user's inventory.")

def planner(request):
    return HttpResponse("This will serve the main purpose: planning your meals.")