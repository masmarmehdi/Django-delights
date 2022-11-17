from django.db.models import Sum
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import *

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    success_url = '/ingredients'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = '/ingredients'

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    context_object_name = 'ingredients'
    success_url = '/ingredients'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'auth/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'auth/logout.html'


class HomeListView(TemplateView):
    template_name = 'inventory/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all() 
        context["purchases"] = Purchase.objects.all() 
        context['recipe_requirements'] = RecipeRequirement.objects.all()
        return context
    
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