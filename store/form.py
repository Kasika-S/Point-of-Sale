from django.forms import ModelForm
from django import forms
from .models import *


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        exclude = ['purchase_date']
        widgets = {
            'sku': forms.TextInput(attrs={'id': 'sku_id'}),
            'quantity': forms.NumberInput(attrs={'id': 'quantity'}),
            'discount': forms.NumberInput(attrs={'id': 'discount', 'step': '.01'}),
            'unit_price': forms.NumberInput(attrs={'id': 'unit_price', 'step': '.01'}),
            'total': forms.NumberInput(attrs={'id': 'total', 'step': '.01'}),
            'expire_date': forms.DateInput(attrs={'id': 'expire_date', 'type': 'date'}),
        }

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        exclude = ['total_sales','best_selling_product']
        widgets = {
            'sku': forms.TextInput(attrs={'id': 'inv_sku_id'}),
        }
class ReservedForm(forms.ModelForm):
    class Meta:
        model = Reserved
        fields = '__all__'

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        exclude = ['sale_date']
        widgets = {
            'quantity': forms.NumberInput(attrs={'id': 'quantity'}),
            'discount': forms.NumberInput(attrs={'id': 'discount', 'step': '.01'}),
            'unit_price': forms.NumberInput(attrs={'id': 'unit_price', 'step': '.01'}),
            'total_amount': forms.NumberInput(attrs={'id': 'total_amount', 'step': '.01'}),
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


