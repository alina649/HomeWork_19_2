from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    """Контроллер, который отвечает за отображение домашней страницы."""
    """Контроллер, который отвечает за отображение информации о продуктах."""
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/catalog.html', context)



def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    return render(request, 'catalog/contacts.html')

def products(request, id):
    """представление страницы main/product.html для каждого продукта"""
    get = get_object_or_404(Product, pk=id)
    product_id = {'products': get}

    return render(request, 'catalog/products.html', product_id)


