from django import forms
from Modulos.Productos.models import Categoria

class CategoriaForm(forms.ModelForm):
    #descripcion = forms.CharField(max_length=30, help_text = "Enter a name")

    class Meta:
        model = Categoria
        fields = ('descripcion','abreviatura',)