# Generated by Django 5.0.3 on 2024-04-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Carrinho', 'verbose_name_plural': 'Carrinhos'},
        ),
    ]
