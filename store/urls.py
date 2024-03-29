from django.urls import path
from .store_views import ( 
    main,
    inventory,
    purchase,
    sales,
    user,
    customer,
)

#URLConfig
urlpatterns = [
    path('dashboard/', main.Dashboard.as_view(), name='dashboard'),
    path('inventory/', inventory.InventoryBoard.as_view(), name='inventory'),
    path('inventory/create', inventory.InventoryBoard.as_view(), name='create_inventory'),
    path('sales/', sales.SaleBoard.as_view(), name='sales'),
    path('sales/create/', sales.SaleBoard.as_view(), name='create_sale'),
    path('purchases/', purchase.PurchaseBoard.as_view(), name='purchases'),
    path('purchases/create/', purchase.PurchaseBoard.as_view(), name='create_purchase'),
    path('users/', user.UserBoard.as_view(), name='users'),
    path('users/create/', user.UserBoard.as_view(), name='create_user'),
    path('customers/', customer.CustomerBoard.as_view(), name='customers'),
    path('customers/create/', customer.CustomerBoard.as_view(), name='create_customer'),
]
