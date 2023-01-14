# Generated by Django 4.1.2 on 2023-01-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_collection_featured_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
        ),
    ]