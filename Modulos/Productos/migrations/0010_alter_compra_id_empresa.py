# Generated by Django 3.2.11 on 2022-07-23 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0009_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.empresa'),
        ),
    ]