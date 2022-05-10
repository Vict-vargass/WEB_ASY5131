from django.urls import path
from .views import home, carrito
#Urls que tendra libreria#

urlpatterns = [
    path ('', home, name= "inicio"),
    path ('carrito', carrito, name="carrito"),

] 

