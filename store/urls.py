from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('dashboard/', views.store_dashboard, name='dashboard'),
]
