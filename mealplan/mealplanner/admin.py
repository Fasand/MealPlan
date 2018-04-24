from django.contrib import admin

from .models import Category, Tag, Nutrition, Unit, Ingredient, Inventory, Recipe

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Nutrition)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Inventory)
admin.site.register(Recipe)