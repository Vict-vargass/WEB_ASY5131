from django import forms
from .models import Libro


class registrarLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['codigo','portada','nombre','stock','precio']
        widgets={
            'codigo': forms.HiddenInput(),
            'portada': forms.HiddenInput(),
            'nombre' : forms.HiddenInput(),
            'stock' : forms.HiddenInput(),
            'precio': forms.HiddenInput(),
        }