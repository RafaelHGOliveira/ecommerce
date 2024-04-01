# Generated by Django 5.0.3 on 2024-04-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_user_genre_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='genre',
            field=models.CharField(max_length=255, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=10, null=True, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='Estado'),
        ),
    ]
