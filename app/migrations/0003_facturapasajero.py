# Generated by Django 4.1.1 on 2022-10-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_serviciospasajeros'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaPasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasajero', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='app.pasajero', verbose_name='Pasajero')),
                ('servicios', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='app.serviciospasajeros', verbose_name='Servicios')),
            ],
        ),
    ]
