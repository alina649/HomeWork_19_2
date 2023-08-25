from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображеие', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категории')
    purchase_price = models.FloatField(verbose_name='цена за пкупку')
    creation_date = models.TimeField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.TimeField(verbose_name='дата последнего изменения', auto_now=True)

    category_product = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, verbose_name='категория')

    def __str__(self):
        return f'{self.name}, {self.purchase_price} rub, {self.description}'

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_current = models.BooleanField(default=True, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

