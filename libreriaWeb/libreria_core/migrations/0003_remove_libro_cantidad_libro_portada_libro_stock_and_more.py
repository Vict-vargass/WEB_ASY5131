# Generated by Django 4.0.4 on 2022-05-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_core', '0002_remove_libro_comprador_alter_libro_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.CharField(max_length=10000, null=True, verbose_name='Portada libro'),
        ),
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.CharField(max_length=2, null=True, verbose_name='cantidad libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.CharField(max_length=10, verbose_name='precio libro'),
        ),
    ]
