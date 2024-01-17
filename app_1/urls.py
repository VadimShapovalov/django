from django.urls import path
from .views import index, contact, client_view

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='about'),
    path('clients/', client_view, name='clients'),
]
