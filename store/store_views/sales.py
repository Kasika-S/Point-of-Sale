from django.views import View
from django.shortcuts import render
from store.models import Sale
from store.form import SaleForm


class SaleBoard(View):
    def get(self, request):
        return render(request, 'sales.html', {'sales': Sale.objects.all()})
    
    def post(self, request):
        
