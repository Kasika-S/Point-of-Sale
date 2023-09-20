from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import Inventory, Purchase
from itertools import chain

class InventoryBoard(View):
    template_name = 'inventory.html'
    contexts = {}
    def get(self, request):
        self.contexts['inventory'] = Purchase.objects.all()
        item_per_page = 10
        paginator = Paginator(self.contexts['inventory'], item_per_page)
        inventory_data = ''
        page = request.GET.get('page')
        try:
            inventory_data = paginator.get_page(page)
            print("".format(inventory_data.has_next())) 
        except PageNotAnInteger:
            inventory_data = paginator.get_page(1)
        except EmptyPage:
            inventory_data = paginator.get_page(paginator.num_pages)

        return render(request, self.template_name, {'inventory_data': inventory_data })





