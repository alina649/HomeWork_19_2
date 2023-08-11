from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображеие', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категории')
    purchase_price = models.FloatField(verbose_name='цена за пкупку')
    creation_date = models.TimeField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.TimeField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.category}, {self.purchase_price} rub, {self.description}'

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

