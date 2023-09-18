from django.views import View
from django.shortcuts import render
from store.models import Inventory
from store.form import InventoryForm

class InventoryBoard(View):
    template_name = 'inventory.html'
    def get(self, request):
        return render(request, 'inventory.html', {'inventory': Inventory.objects.all()})

    def post(self,request):
        inventory_form = InventoryForm(request.POST)
        if(inventory_form.is_valid()):
            inventory_form.save()
            return redirect('inventory')
        return render(request, self.template_name, {'inventory_form': inventory_form})




