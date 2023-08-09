from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Удаление старых данных...')
        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write('Создание категории...')
        Category.objects.create(name='Телефоны', description='новинки 2022')
        Category.objects.create(name='Ноутбуки', description='новинки 2023')


        self.stdout.write('Создание продукта...')
        category1 = Category.objects.get(name='Телефоны')
        Product.objects.create(name='Samsung', description='прослужит долго',
                                purchase_price=100, category=category1)

        category2 = Category.objects.get(name='Ноутбуки')
        Product.objects.create(name='ARDOR', description='игровой ноутбук',
                                purchase_price=200, category=category2)

        self.stdout.write(self.style.SUCCESS('База успешно заполнена!'))

