# Generated by Django 4.2.3 on 2023-08-24 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_purchase_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
    ]