# Generated by Django 3.2.11 on 2022-07-20 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0007_compra_id_forma_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.proveedor'),
        ),
    ]