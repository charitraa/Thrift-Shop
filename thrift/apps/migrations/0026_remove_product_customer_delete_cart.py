# Generated by Django 5.0.1 on 2024-03-31 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_alter_product_customer_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]