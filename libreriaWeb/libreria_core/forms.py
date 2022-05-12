from django import forms
from .models import Carrito, Libro


class registrarLibro(forms.ModelForm):

    class Meta:
        model = Carrito
        fields = ['codigo','nombre','cantidad','precio']
        widgets={
            'codigo': forms.HiddenInput(),
            'nombre' : forms.HiddenInput(),
            'cantidad' : forms.HiddenInput(),
            'precio': forms.HiddenInput(),
        }