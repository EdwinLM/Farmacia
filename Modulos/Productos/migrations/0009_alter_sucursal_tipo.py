# Generated by Django 3.2.11 on 2022-05-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0008_alter_sucursal_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='tipo',
            field=models.CharField(help_text='C = Centro de Distribución, S = Sucursal', max_length=1),
        ),
    ]
