from django.db import models

class Libro (models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="codigo", null=False)
    portada = models.CharField(max_length=10000, verbose_name="Portada libro", null=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre libro")
    stock = models.IntegerField(verbose_name="stock libro", null=True)
    precio= models.CharField(max_length=1000000,verbose_name="precio libro")
    def __str__(self):
        return self.codigo




class Carrito (models.Model):
    codigoCarrito = models.CharField(max_length=3,primary_key=True, verbose_name="codigo del carro", null=False)
    codigoLibro = models.ManyToManyField( Libro, verbose_name="codigo del libro")
    cantidad = models.IntegerField(verbose_name="cantidad de libros", null=True)
    def __str__(self):
        return str(self.codigoCarrito)