from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('main/', views.store_main, name='main'),
    path("dashboard/", views.store_main, name='dashboard'),
    path("users/", views.users, name='users'),
    path("purchases/", views.purchases, name='purchases'),
    path("sales/", views.sales, name='sales'),
    path("inventory/", views.inventory, name='inventory'),
    path("reports/", views.reports, name='reports'),
]
