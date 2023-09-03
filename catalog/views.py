from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm, ProductModerForm
from catalog.models import Product, Version
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Если пользователь аутентифицирован (в том числе владелец товара)
            if user.is_staff or user.is_superuser:
                # Для администраторов показываем все продукты
                queryset = super().get_queryset()

            else:
                # Для остальных аутентифицированных пользователей
                queryset = super().get_queryset().filter(
                    status=Product.STATUS_PUBLISH
                )
        else:
            # Для неаутентифицированных пользователей
            queryset = super().get_queryset().filter(
                status=Product.STATUS_PUBLISH
            )
        return queryset


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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductModerForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if self.object.owner != self.request.user:
            if user.is_staff:
                return self.object
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)







