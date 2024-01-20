from django.urls import path
from .views import index, contact, client_view, all_client_orders, order_sort_time

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='about'),
    path('clients/', client_view, name='clients'),
    path('orders/<int:client_id>/', all_client_orders, name='all_client_orders'),
    path('products/<int:client_id>/<int:days>/', order_sort_time, name='order_sort_time'),
]