from django.db import models

class Libro (models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="codigo", null=False)
    portada = models.CharField(max_length=10000, verbose_name="Portada libro", null=True)
    nombre = models.CharField(max_length=100, verbose_name="nombre libro")
    stock = models.IntegerField(verbose_name="stock libro", null=True)
    precio= models.IntegerField(verbose_name="precio libro")
    def __str__(self):
        return self.codigo




class Carrito (models.Model):
    codigoCarrito = models.CharField(max_length=3,primary_key=True, verbose_name="codigo del carro", null=False)
    fecha = models.DateField(verbose_name="fecha", null=True)
    def __str__(self):
        return str(self.codigoCarrito)


class Detail (models.Model):
    codigoCarro = models.ForeignKey(Carrito, verbose_name="Codigo del Carro", on_delete=models.CASCADE)
    codigoLibro = models.ForeignKey(Libro, verbose_name="Codigo del Libro", on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="Cantidad del libro")