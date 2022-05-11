from django import forms
from .models import Libro

class actualizarCarro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['codigo','nombre','cantidad','precio']
        widgets={
            'codigo': forms.TextInput(attrs={'class':'form-control','placeholder':'cod'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':''}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':''}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
        }


class registrarLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['codigo','nombre','cantidad','precio']
        widgets={
            'codigo': forms.HiddenInput(),
            'nombre' : forms.HiddenInput(),
            'cantidad' : forms.HiddenInput(),
            'precio': forms.HiddenInput(),
        }