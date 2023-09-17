from django.views import View
from django.shortcuts import render
from store.models import Purchase, Inventory
from store.form import PurchaseForm, InventoryForm


class PurchaseBoard(View):

    template_name = 'purchases.html'

    def get(self, request):
        purchase_form = PurchaseForm()
        inventory_form = InventoryForm()
        return render(request, self.template_name, {'purchase_form':purchase_form,'inventory_form': inventory_form})

    def post(self, request):
        purchase_form = PurchaseForm(request.POST)
        inventory_form = InventoryForm(request.POST)

        if purchase_form.is_valid() and inventory_form.is_valid():
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
            inventory_fields = {
                'sku': inventory_form.cleaned_data['sku'],
                'item_name': inventory_form.cleaned_data['item_name'],
                'item_description': inventory_form.cleaned_data['item_description'],
                'category': inventory_form.cleaned_data['category'],
                'uom': inventory_form.cleaned_data['uom'],
                'reorder_point': inventory_form.cleaned_data['reorder_point'],
                'total_purchases': inventory_form.cleaned_data['total'],
                'stock_available_main': inventory_form.cleaned_data['stock_available_main'],
                'stock_available_for_sale': inventory_form.cleaned_data['stock_available_main'],
                'stock_available_value': purchase_form.cleaned_data['quality'] * purchase_form.cleaned_data['unit_price'] if (inventory_form.cleaned_data['stock_available_main'] == 0) else purchase_form.cleaned_data['unit_price'] * inventory_form.cleaned_data['stock_available_main'],

            }
            Purchase.objects.create(**purchase_fields)
            Inventory.objects.create(**inventory_fields)
            Purchase.save()
            Inventory.save()
            return redirect('purchases')

        return render(request, self.template_name, {'purchase_form':purchase_form,'inventory_form':inventory_form})

