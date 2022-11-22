from django import forms
from .models import *
from django.core.exceptions import ValidationError

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')
        labels = {
            'quantity': 'Amount needed',
            'unit_price': 'Price per unit'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'unit': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError("quantity must be more than 0")
        return quantity

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price')
        labels = {
            'title': 'Menu name: ',
            'price': 'Considered price: '
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'price': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
        }

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')

        widgets = {
            'menu_item': forms.Select(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'ingredient': forms.Select(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'})
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item',)

        widgets = {
            'menu_item': forms.Select(attrs={'class': 'form-control col-md-4', 'style': 'margin:0 auto;'}),
        }