from django.views import View
from django.shortcuts import render, redirect
from store.models import Sale
from store.form import SaleForm


class SaleBoard(View):
    contexts = {}
    def get(self, request):
        self.contexts['sale_form'] = SaleForm()
        self.contexts['sale_data'] = Sale.objects.all()

        return render(request, 'sales.html', {**self.contexts})

    def post(self, request):
        self.contexts['sale_form'] = SaleForm(request.POST)
        if(self.contexts['sale_form'].is_valid()):
            self.contexts['sale_form'].save()
            return redirect('sales')
        else:
            print(self.contexts['sale_form'].errors)
        return render(request, 'sales.html', {**self.contexts  })

