from django.views import View
from django.shortcuts import render 
from store.models import Customer

class CustomerBoard(View):
    def get(self, request):
        return render(request, 'customers.html', {'customers': Customer.objects.all()})

