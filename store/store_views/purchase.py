from django.views import View
from django.shortcuts import render, redirect
from store.models import Purchase, Inventory
from store.form import PurchaseForm, InventoryForm


class PurchaseBoard(View):
    template_name = 'purchases.html'
    def get(self, request):
        purchase_form = PurchaseForm()
        inventory_form = InventoryForm()
        return render(request, self.template_name,{'purchase_form': purchase_form,'inventory_form':inventory_form})
    def post(self, request):
        purchase_form = PurchaseForm(request.POST)
        inventory_form = InventoryForm(request.POST)
        if(purchase_form.is_valid()):
            purchase_instance = purchase_form.save(commit=False)
            if inventory_form.is_valid():
                inventory_instance = inventory_form.save(commit=False)
                purchase_instance.save()
                inventory_instance.save()
            return redirect('inventory')
        return render(request, self.template_name, {'purchase_form': purchase_form, 'inventory_form': inventory_form })

