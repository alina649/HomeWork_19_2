# Generated by Django 4.2.3 on 2023-09-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_product_category_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_product_status', 'Can change the status of products'), ('change_product_description', 'Can change product description'), ('change_product_category', 'Can change product category')], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('created', 'Добавлен'), ('moderated', 'На модерации'), ('published', 'Опубликован')], default='moderated', max_length=20, verbose_name='статус'),
        ),
    ]
