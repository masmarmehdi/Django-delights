from django import forms
from .models import Ingredient
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
        
        