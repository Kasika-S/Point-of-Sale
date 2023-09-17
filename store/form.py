from django import forms
from .models import *



'''
 purchase_fields = {
                'sku': purchase_form.cleaned_data['sku'],
                'purchase_order': purchase_form.cleaned_data['purchase_order'],
                'purchase_date': purchase_form.cleaned_data['purchase_date'],
                'supplier': purchase_form.cleaned_data['supplier'],
                'quantity': purchase_form.cleaned_data['quantity'],
                'discount': purchase_form.cleaned_data['discount'],
                'unit_price': purchase_form.cleaned_data['unit_price'],
                'total': purchase_form.cleaned_data['total'],
                'expire_date': purchase_form.cleaned_data['expire_date'],
            }
'''
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'quantity': forms.NumberInput(attrs={'id': 'quantity'}),
            'discount': forms.NumberInput(attrs={'id': 'discount', 'step': '.01'}),
            'unit_price': forms.NumberInput(attrs={'id': 'unit_price', 'step': '.01'}),
            'total': forms.NumberInput(attrs={'id': 'total', 'step': '.01'}),
            'expire_date': forms.DateInput(attrs={'id': 'expire_date', 'type': 'date'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ['total_sales','best_selling_product']
class ReservedForm(forms.ModelForm):
    class Meta:
        model = Reserved
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['sale_date']
        widgets = {
            'quantity': forms.NumberInput(attrs={'id': 'quantity'}),
            'discount': forms.NumberInput(attrs={'id': 'discount', 'step': '.01'}),
            'unit_price': forms.NumberInput(attrs={'id': 'unit_price', 'step': '.01'}),
            'total_amount': forms.NumberInput(attrs={'id': 'total_amount', 'step': '.01'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


