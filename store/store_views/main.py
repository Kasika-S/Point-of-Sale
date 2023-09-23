from django.views import View
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from store.models import *


class Dashboard(View):
    template = 'index.html'
    contexts = {}

    ## dates
    today = timezone.now()
    yesterday = today - timedelta(days=1)
    week = today -  timedelta(days=7)
    month = today - timedelta(days=30)
    threeMonth = today - timedelta(days=90)

    # monthly
    now = datetime.now();
    start_date = datetime(now.year, now.month, 1)
    next_month = now.month + 1 if now.month < 12 else 1
    end_date = datetime(now.year, next_month, 1)
    def get(self, request):
        self.contexts['sales']  = Sale.objects.all()
        self.contexts['products'] = Purchase.objects.all()
        self.contexts['customers'] = Customer.objects.all()
        self.contexts['inventory'] = Inventory.objects.all()
        self.contexts['sale_history'] = Sale.objects.all().order_by('sale_date')[:5]
        self.contexts['total_sum'] = Sale.objects.all().aggregate(Sum('total_amount'))['total_amount__sum']
        self.contexts['monthly_amount'] = Sale.objects.filter(sale_date__gte=self.start_date, sale_date__lte=self.end_date)\
            .aggregate(Sum('total_amount'))['total_amount__sum']
        # order counts
        self.contexts['day'] = Sale.objects.filter(sale_date=self.today).count()
        self.contexts['day_amount'] = Sale.objects.filter(sale_date=self.today).aggregate(Sum('total_amount'))['total_amount__sum']
        self.contexts['yesterday'] = Sale.objects.filter(sale_date=self.yesterday).count()
        self.contexts['yesterday_amount'] = Sale.objects.filter(sale_date=self.yesterday).aggregate(Sum('total_amount'))['total_amount__sum']
        self.contexts['week'] = Sale.objects.filter(sale_date=self.week).count()
        self.contexts['week_amount'] = Sale.objects.filter(sale_date=self.week).aggregate(Sum('total_amount'))['total_amount__sum']
        self.contexts['month'] = Sale.objects.filter(sale_date=self.month).count()
        self.contexts['month_amount'] = Sale.objects.filter(sale_date=self.month).aggregate(Sum('total_amount'))['total_amount__sum']
        self.contexts['threeMonth'] = Sale.objects.filter(sale_date=self.threeMonth).count()
        self.contexts['threeMonth_amount'] = Sale.objects.filter(sale_date=self.threeMonth).aggregate(Sum('total_amount'))['total_amount__sum']
        return render(request, self.template, self.contexts)



