from django.db import models

class Libro (models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="codigo", null=False)
    portada = models.CharField(max_length=10000, verbose_name="Portada libro", null=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre libro")
    stock = models.IntegerField(max_length=2, verbose_name="stock libro", null=True)
    precio= models.CharField(max_length=10, verbose_name="precio libro")
    def __str__(self):
        return self.codigo




class Carrito (models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="codigo", null=False)
    nombre = models.CharField(max_length=100, verbose_name="nombre libro")
    cantidad = models.IntegerField(max_length=2, verbose_name="cantidad libro", null=True)
    precio= models.CharField(max_length=10, verbose_name="precio libro")
    def __str__(self):
        return self.codigo