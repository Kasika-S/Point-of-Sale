from django.shortcuts import render
from django.http import HttpResponse
from store.models import User
# Create your views here.

def store_main(request):
    return render(request, 'index.html')

def store_dashboard(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'customers.html', {'users': User.objects.all()})

def purchases(request):
    return render(request, 'purchases.html')

def sales(request):
    return render(request, 'sales.html')

def inventory(request):
    return render(request, 'items.html')
def reports(request):
    return render(request, 'reports.html')



