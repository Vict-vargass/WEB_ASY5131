from django.contrib import admin
from libreria_core.models import Libro, Carrito, Detail
# Register your models here.

admin.site.register(Libro)
admin.site.register(Carrito)
admin.site.register(Detail)