import json
from django.views import View
from django.shortcuts import render, redirect
from store.models import Purchase, Inventory
from store.form import PurchaseForm


class PurchaseBoard(View):
    template_name = 'purchases.html'
    contexts = {}
    def get(self, request):
        self.contexts['purchase_form'] = PurchaseForm()
        return render(request, self.template_name,{**self.contexts})
    def post(self, request):
        self.contexts['purchase_form'] = PurchaseForm(request.POST)

        if(self.contexts['purchase_form'].is_valid()):
            self.contexts['purchase_form'].save()
            return redirect('Inventory')

        else:
            print(self.contexts['purchase_form'].errors)
        return render(request, self.template_name, { **self.contexts })

