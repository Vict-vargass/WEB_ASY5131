from rest_framework import serializers
from libreria_core.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Libro
        fields = ['codigo','nombre','cantidad','precio','comprador']