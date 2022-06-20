from rest_framework import serializers
from libreria_core.models import Detail, Carrito

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Detail
        fields = ['codigoCarro','codigoLibro','cantidad',]

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carrito
        fields = ['codigoCarrito','fecha',]