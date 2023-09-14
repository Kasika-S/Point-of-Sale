from django.views import View
from django.shortcuts import render
from store.models import Inventory

class InventoryBoard(View):
    def get(self, request):
        return render(request, 'inventory.html', {'inventory': Inventory.objects.all()})


