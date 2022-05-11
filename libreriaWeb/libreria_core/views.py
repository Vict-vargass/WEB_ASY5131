from dataclasses import field
from distutils.log import error
from html.entities import codepoint2name
from pickle import TRUE
import string
from django.shortcuts import render
from libreria_core.models import Libro
from libreria_core.forms import registrarLibro 
import urllib, json
# Create your views here.
# Aca se crean las vistas y se le da nombre a la url, 
# se implementan las acciones en general


def home(request):

    url = "https://gaff8f4466ad45b-library01db.adb.sa-santiago-1.oraclecloudapps.com/ords/admin/libro/"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    cod1 = 'MDD021'
    cod2 = 'AFK204'
    cod3 = 'CAS211'
    cod4 = 'DLY402'
    form1 = registrarLibro(initial={'codigo': cod1,'nombre':'American Psycho','cantidad': '1','precio':'18000'})
    form2 = registrarLibro(initial={'codigo': cod2,'nombre':'Dune','cantidad':'1', 'precio':'5000'})
    form3 = registrarLibro(initial={'codigo':cod3,'nombre':'Jujutsu Kaisen 1','cantidad':'1','precio':'10000'})
    form4 = registrarLibro(initial={'codigo':cod4,'nombre':'Jujutsu Kaisen 0','cantidad':'1','precio':'14500'})
    

    datos = {
        'data' : data,
        'form1' : form1,
        'form2' : form2,
        'form3' : form3,
        'form4' : form4,

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