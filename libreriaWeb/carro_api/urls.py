from django.urls import path
from carro_api.views import carritos, carro, detalles

urlpatterns = [
    path('carrito', carritos, name='carrito'),
    path('libro-carro/<pk>', carro, name='libro-carro'),
    path('detalles', detalles, name="detalles")
]