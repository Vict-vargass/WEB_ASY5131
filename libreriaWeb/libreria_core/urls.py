from django.urls import path
from .views import home, ingresarLibros
#Urls que tendra libreria#

urlpatterns = [
    path ('', home, name= "inicio"),
    path ('ingresarLibro', ingresarLibros, name="ingresar_libro"),

] 

