# Generated by Django 5.0.3 on 2024-03-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]