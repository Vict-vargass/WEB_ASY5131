# Generated by Django 4.0.4 on 2022-05-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_core', '0006_remove_carrito_codigo_remove_carrito_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='codigoCarrito',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='codigo del carro'),
        ),
    ]
