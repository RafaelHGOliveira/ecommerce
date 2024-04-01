# Generated by Django 5.0.3 on 2024-04-01 20:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_user_address_alter_user_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255, null=True, verbose_name='Estado')),
                ('city', models.CharField(max_length=255, null=True, verbose_name='Cidade')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Endereço')),
                ('number', models.CharField(max_length=10, null=True, verbose_name='Numero')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
