from django.shortcuts import render
from django.http import HttpResponse
from store.models import User, Inventory, Sale, Purchase
# Create your views here.

def store_main(request):
    return render(request, 'index.html')

def store_dashboard(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'customers.html', {'users': User.objects.all()})

def purchases(request):
    return render(request, 'purchases.html', {'purchases':Purchase.objects.all()})

def sales(request):
    return render(request, 'sales.html', {'sales': Sale.objects.all()})

def inventory(request):
    return render(request, 'inventory.html', {'inventory': Inventory.objects.all()})
def reports(request):
    return render(request, 'reports.html')


#TODO: make it more robust and secure(fetching process)
