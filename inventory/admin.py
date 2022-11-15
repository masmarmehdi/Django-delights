from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

@admin.register(Ingredient)
class IngeredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'unit_price')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'timestamp')
