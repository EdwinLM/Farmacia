# Generated by Django 3.2.11 on 2022-07-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0011_alter_venta_id_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='indicaciones',
            field=models.ManyToManyField(to='Productos.Indicacion'),
        ),
    ]