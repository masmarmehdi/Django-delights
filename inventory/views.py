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

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = '/menu-items'

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = '/menu-items'

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete.html'
    success_url = '/menu-items'


class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    context_object_name = 'recipe_requirements'

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = '/recipe-requirements'

class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = '/recipe-requirements'

class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_delete.html'
    success_url = '/recipe-requirements'

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchases'
    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchases.html'
    context_object_name = 'purchases'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost
        return context