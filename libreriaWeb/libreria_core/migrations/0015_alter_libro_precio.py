# Generated by Django 4.0.4 on 2022-06-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_core', '0014_detail_delete_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.IntegerField(verbose_name='precio libro'),
        ),
    ]