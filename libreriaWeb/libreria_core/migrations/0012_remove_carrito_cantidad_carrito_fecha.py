# Generated by Django 4.0.4 on 2022-06-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_core', '0011_remove_carrito_codigolibro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='carrito',
            name='fecha',
            field=models.IntegerField(null=True, verbose_name='fecha'),
        ),
    ]
