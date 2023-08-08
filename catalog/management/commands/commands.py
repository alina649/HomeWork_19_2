from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'name': 'Samsung', 'description': 'Телефон'},
            {'name': 'ARDOR', 'description': 'Ноутбук'},
            {'name': 'Ракета', 'description': 'Часы'},
            {'name': 'Redmi', 'description': 'Телефон'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)


