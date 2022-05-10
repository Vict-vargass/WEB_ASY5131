from django.shortcuts import render
from libreria_core.models import Libro
from libreria_core.forms import registrarVenta, registrarLibro 
import urllib, json

# Create your views here.
# Aca se crean las vistas y se le da nombre a la url, 
# se implementan las acciones en general


def home(request):
    url = "https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    codigo = ""
    nombre = ""
    form = registrarVenta(initial={'codigo': codigo, 'nombre': nombre})
    
    
    datos = {
        'form': form,
        'data': data,
        'n' : range(12),
        'formulario1': registrarLibro,
        'codigo' : codigo
    }

        
    return render(request, 'libreria_core/prueba.html', datos)


def carrito(request):
    
    url = "https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/AFK230"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    datos = {
        'data': data
    }

    
    return render (request, 'libreria_core/carrito.html', datos)