# Generated by Django 4.1.1 on 2022-10-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_facturapasajero'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturapasajero',
            name='formaPago',
            field=models.CharField(choices=[['efectivo', 'efectivo'], ['Debito', 'Debito']], default='No Desea', max_length=50, verbose_name='formaPago'),
        ),
    ]
