# Generated by Django 3.2.11 on 2022-07-11 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_auto_20220622_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]