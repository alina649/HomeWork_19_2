from django import forms

from catalog.models import Product, Version


FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта',
                   'биржа', 'дешево', 'бесплатно', 'обман',
                   'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_current":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'purchase_price', 'category_product',)

    def clean(self):

        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and any(word in name.lower() for word in FORBIDDEN_WORDS):
            self.add_error('name', 'Недопустимое слово в названии продукта.')

        if description and any(word in description.lower() for word in FORBIDDEN_WORDS):
            self.add_error('description', 'Недопустимое слово в описании продукта')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'