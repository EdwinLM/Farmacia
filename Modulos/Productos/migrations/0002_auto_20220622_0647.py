# Generated by Django 3.2.11 on 2022-06-22 06:47

import Modulos.Productos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='id_forma_pago',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Productos.forma_pago'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_corto',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre corto para facturación', max_length=24, unique=True),
        ),
    ]
