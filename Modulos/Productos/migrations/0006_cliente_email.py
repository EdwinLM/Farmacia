# Generated by Django 3.2.11 on 2022-07-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_auto_20220714_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='sc@gmail.com', max_length=100),
        ),
    ]