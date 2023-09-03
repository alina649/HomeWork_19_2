from django.conf import settings
from django.db import models

from blog.models import NULLABLE


class Product(models.Model):
    STATUS_CREATED = 'created'
    STATUS_MODERATED = 'moderated'
    STATUS_PUBLISH = 'published'
    STATUSES = (
        (STATUS_CREATED, 'Добавлен'),
        (STATUS_MODERATED, 'На модерации'),
        (STATUS_PUBLISH, 'Опубликован'),
    )

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображеие', null=True, blank=True)
    purchase_price = models.FloatField(verbose_name='цена за пкупку')
    creation_date = models.TimeField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.TimeField(verbose_name='дата последнего изменения', auto_now=True)
    category_product = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, verbose_name='категория')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_MODERATED, verbose_name='статус')

    def __str__(self):
        return f'{self.name}, {self.purchase_price} rub, {self.description}'

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

        ordering = ('name',)
        permissions = [
            ('set_product_status', 'Can change the status of products'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category'),
        ]


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

