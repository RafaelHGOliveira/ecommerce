# Generated by Django 5.0.4 on 2024-04-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_name_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Nome'),
        ),
    ]
