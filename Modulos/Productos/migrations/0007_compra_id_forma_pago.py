# Generated by Django 3.2.11 on 2022-07-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0006_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='id_forma_pago',
            field=models.IntegerField(choices=[(1, 'CONTADO'), (2, 'CREDITO')], default=1),
        ),
    ]
