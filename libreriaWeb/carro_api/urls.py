from django.urls import path
from carro_api.views import carrito

urlpatterns = [
    path('libros', carrito, name='libros'),
]