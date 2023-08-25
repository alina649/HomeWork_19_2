from django.urls import path
from . import views
from catalog.views import IndexListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', contacts),
    path('products/<int:pk>/', ProductDetailView.as_view() , name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]