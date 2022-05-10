from django.db import models

class Libro (models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="codigo")
    nombre = models.CharField(max_length=100, verbose_name="nombre libro")
    cantidad = models.CharField(max_length=2, verbose_name="stock libro")
    precio= models.CharField(max_length=10, verbose_name="precio libro")
    comprador = models.CharField(max_length=100, verbose_name="comprador")
    def __str__(self):
        return self.codigo
