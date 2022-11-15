from django.db.models import Sum
from django.views.generic import ListView
from .models import *

class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredients'

class MenuItemListView(ListView):
    model = MenuItem
    context_object_name = 'menu_items'
class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    context_object_name = 'recipe_requirements'

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchases.html'
    context_object_name = 'purchases'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cost = 0
        profit = 0
        revenue = 0
        purchase = Purchase.objects.all()
        quantity_used = RecipeRequirement.objects.all()

        for recipe in quantity_used:
            cost += recipe.ingredient.unit_price * recipe.quantity
        for item in purchase:
            revenue += item.menu_item.price

        profit = revenue - cost * purchase.count()
        context['revenue'] = revenue
        context['cost'] = cost * purchase.count()
        context['profit'] = profit
        return context