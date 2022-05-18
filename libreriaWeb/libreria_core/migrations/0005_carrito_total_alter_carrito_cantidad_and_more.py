# Generated by Django 4.0.4 on 2022-05-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_core', '0004_carrito_alter_libro_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='total',
            field=models.IntegerField(null=True, verbose_name='total del carro'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cantidad',
            field=models.IntegerField(null=True, verbose_name='cantidad libro'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='precio',
            field=models.IntegerField(verbose_name='precio libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='stock',
            field=models.IntegerField(null=True, verbose_name='stock libro'),
        ),
    ]