from django.urls import path
from .views import *
urlpatterns = [
    path('ingredients/', IngredientListView.as_view()),
    path('menu-items/', MenuItemListView.as_view()),
    path('recipe-requirements/', RecipeRequirementListView.as_view()),
    path('purchases/', PurchaseListView.as_view())
]
