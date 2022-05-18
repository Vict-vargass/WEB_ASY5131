from django.urls import path
from carro_api.views import carrito, libro_carro

urlpatterns = [
    path('carrito', carrito, name='carrito'),
    path('libro-carro/<pk>', libro_carro, name='libro-carro')
]