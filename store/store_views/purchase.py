from django.views import View
from django.shortcuts import render 
from store.models import Purchase


class PurchaseBoard(View):
    def get(self, request):
        return render(request, 'purchases.html', {'purchases': Purchase.objects.all()})

