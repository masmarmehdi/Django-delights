from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view()),
    path('ingredients/', IngredientListView.as_view()),
    path('menu-items/', MenuItemListView.as_view()),
    path('recipe-requirements/', RecipeRequirementListView.as_view()),
    path('purchases/', PurchaseListView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout')
]
