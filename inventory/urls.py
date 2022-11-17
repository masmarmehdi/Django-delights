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
    path('ingredients/delete/<int:pk>', IngredientDeleteView.as_view(), name='delete-ingredient')
]
