from django.urls import path
from . import views
from catalog.views import IndexListView, contacts, ProductDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contacts),
    path('products/<int:pk>/', ProductDetailView.as_view() , name='products'),
]