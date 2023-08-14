from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from catalog.models import Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'



def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'

    def products(self, request, id):
        """представление страницы main/product.html для каждого продукта"""
        get = get_object_or_404(Product, pk=id)
        product_id = {'products': get}

        return render(request, self.template_name, product_id)



