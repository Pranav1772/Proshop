# Generated by Django 5.0.1 on 2024-01-07 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='coutnInStock',
            new_name='countInStock',
        ),
    ]