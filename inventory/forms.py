from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')
        labels = {
            'quantity': 'Amount needed',
            'unit_price': 'Price per unit'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
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
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')

        widgets = {
            'menu_item': forms.Select(attrs={'class': 'form-control'}),
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item',)

        widgets = {
            'menu_item': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_ids = [item.id for item in MenuItem.objects.all() if item.available()]
        self.fields['menu_item'].queryset = MenuItem.objects.filter(id__in=available_ids)
        self.fields['menu_item'].label = 'Select Menu Item'


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class BootstrapUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'