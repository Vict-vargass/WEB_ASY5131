from django.shortcuts import render
from libreria_core.models import Libro
from libreria_core.forms import registrarLibro 
# Create your views here.
# Aca se crean las vistas y se le da nombre a la url, 
# se implementan las acciones en general


def home(request):

    libros = Libro.objects.all()
    formu = registrarLibro()
    datos = {
        'libros': libros,
        'form': formu
    }

    if request.method=='POST':
        form = registrarLibro(request.POST)
        if form.is_valid():
            form.save()
            
        
    return render(request, 'libreria_core/home.html', datos)


def carrito(request):
    
    carro = Libro.objects.all()
    datos = {
        'carro' : carro
    }

    return render (request, 'libreria_core/carrito.html', datos)