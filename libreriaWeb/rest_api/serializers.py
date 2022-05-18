from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from libreria_core.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Libro
        fields = ['codigo','nombre','portada','stock','precio']


class UpdateStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['stock']