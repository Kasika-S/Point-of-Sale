from django.views import View
from django.shortcuts import render
from store.models import Sale
from store.form import SaleForm


class SaleBoard(View):
    def get(self, request):
        sale_form = SaleForm()
        return render(request, 'sales.html', {'sale_form': sale_form})

def post(self, request):
    sale_form = SaleForm()

    if(sale_form.is_valid()):
        sale_fields = {
            'sale_order': sale_form.cleaned_data['sale_order'],
            'sale_date': sale_form.cleaned_data['sale_date'],
            'sku': sale_form.cleaned_data['sku'],
            'quantity': sale_form.cleaned_data['quantity'],
            'discount': sale_form.cleaned_data['discount'],
            'unit_price': sale_form.cleaned_data['unit_price'],
            'total_amount': sale_form.cleaned_data['total_amount'],
        }
        sale = Sale(**sale_fields)
        sale.save()
        return redirect('sales')
    return render(request, 'sales.html', {'sale_form': sale_from })
