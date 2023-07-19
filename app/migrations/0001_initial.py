# Generated by Django 4.1.1 on 2022-10-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutOpasaporte', models.CharField(max_length=30, verbose_name='Rut o Pasaporte')),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('direccion', models.CharField(max_length=300, verbose_name='Direccion')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('pais', models.CharField(max_length=100, verbose_name='Pais')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('nHabitacion', models.CharField(choices=[['101', '101'], ['102', '102'], ['103', '103'], ['204', '204'], ['205', '205'], ['206', '206'], ['307', '307'], ['308', '308'], ['309', '309']], max_length=50, verbose_name='Numero Habitacion')),
                ('tipoHabitacion', models.CharField(choices=[['Single', 'Single'], ['Doble', 'Doble'], ['Queen', 'Queen'], ['King', 'King']], max_length=50, verbose_name='Tipo de Habitacion')),
                ('cantidadNinos', models.PositiveIntegerField(default=0, verbose_name='Cantidad Niños')),
                ('cantidadAdultos', models.PositiveIntegerField(default=0, verbose_name='Cantidad Adultos')),
                ('llegada', models.DateField(verbose_name='Llegada')),
                ('salida', models.DateField(verbose_name='Salida')),
            ],
        ),
    ]