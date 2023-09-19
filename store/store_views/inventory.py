from django.views import View
from django.shortcuts import render
from store.models import Inventory
from store.form import InventoryForm

class InventoryBoard(View):
    template_name = 'inventory.html'
    contexts = {}
    def get(self, request):
        self.contexts['inventory'] = Inventory.objects.all()
        return render(request, 'inventory.html', {**self.contexts})

    def post(self,request):
        self.contexts['inventory_form'] = InventoryForm(request.POST)
        if(self.contexts['inventory_form'].is_valid()):
            inventory_form.save()
            return redirect('inventory')
        else:
            print(self.contexts['inventory_form'].errors)
        return render(request, self.template_name, {**self.contexts})




