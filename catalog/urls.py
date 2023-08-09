from django.urls import path
from . import views
from catalog.views import index, contacts, products

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/<int:id>/', products, name='products'),
]