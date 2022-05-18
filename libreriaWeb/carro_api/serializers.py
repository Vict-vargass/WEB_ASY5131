from rest_framework import serializers
from libreria_core.models import Carrito

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carrito
        fields = ['codigoCarrito', 'codigoLibro','nombre','cantidad','precio', 'url']



class CarroUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carrito
        fields = ['codigoLibro','nombre','cantidad','precio']