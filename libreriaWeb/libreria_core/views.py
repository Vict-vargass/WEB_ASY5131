from django.shortcuts import render
from libreria_core.models import Libro
# Create your views here.
# Aca se crean las vistas y se le da nombre a la url, 
# se implementan las acciones en general


def home(request):

    libros = Libro.objects.all()
    datos = {
        'libros': libros,
    }

    return render(request, 'libreria_core/inicio.html', datos)


def carrito(request):
    
    carro = Libro.objects.all()
    datos = {
        'carro' : carro
    }

    return render (request, 'libreria_core/carrito.html', datos)