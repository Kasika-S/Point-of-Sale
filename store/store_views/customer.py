from django.views import View
from django.shortcuts import render, redirect
from store.models import Customer
from store.form import CustomerForm

class CustomerBoard(View):
    contexts = {}
    def get(self, request):
        self.contexts['form'] = CustomerForm()
        self.contexts['customers'] = Customer.objects.all()
        return render(request, 'customers.html', {**self.contexts })
    def post(self,request):
        self.contexts['form'] = CustomerForm(request.POST)
        if self.contexts['form'].is_valid():
            self.contexts['form'].save()
            return redirect('customers')
        else:
            print(self.contexts['form'].errors)
        return render(request, 'customers.html', {**self.contexts })

