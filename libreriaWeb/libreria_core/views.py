from django.shortcuts import render, redirect

# Create your views here.
# Aca se crean las vistas y se le da nombre a la url, 
# se implementan las acciones en general


def home(request):
    return render(request, 'libreria_core/home.html')


def ingresarLibros(request):
    return render (request, 'libreria_core/ingresarLibro.html')