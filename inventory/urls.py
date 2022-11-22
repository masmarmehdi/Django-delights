from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('ingredients/', IngredientListView.as_view(), name='ingredients'),
    path('menu-items/', MenuItemListView.as_view(), name='menu-items'),
    path('recipe-requirements/', RecipeRequirementListView.as_view(), name='recipe-requirements'),
    path('purchases/', PurchaseListView.as_view(), name='purchases'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout'),
    path('ingredients/create', IngredientCreateView.as_view(), name='create-ingredient'),
    path('ingredients/edit/<int:pk>', IngredientUpdateView.as_view(), name='update-ingredient'),
    path('ingredients/delete/<int:pk>', IngredientDeleteView.as_view(), name='delete-ingredient'),
    path('menu-items/create', MenuItemCreateView.as_view(), name='create-menu_items'),
    path('menu-items/edit/<int:pk>', MenuItemUpdateView.as_view(), name='update-menu_items'),
    path('menu-items/delete/<int:pk>', MenuItemDeleteView.as_view(), name='delete-menu_items'),
    path('recipe-requirements/create/', RecipeRequirementCreateView.as_view(), name='create-recipe_requirement'),
    path('recipe-requirements/edit/<int:pk>', RecipeRequirementUpdateView.as_view(), name='update-recipe_requirement'),
    path('recipe-requirements/delete/<int:pk>', RecipeRequirementDeleteView.as_view(), name='delete-recipe_requirement'),
    path('purchases/create', PurchaseCreateView.as_view(), name='create-purchase')
]
