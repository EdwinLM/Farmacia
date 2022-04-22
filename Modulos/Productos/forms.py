from django import forms
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Pais, Unidad_Medida, Via_Administracion, Tipo_Prescripcion

class CategoriaForm(forms.ModelForm):
    #descripcion = forms.CharField(max_length=30, help_text = "Enter a name")

    class Meta:
        model = Categoria
        fields = ('descripcion','abreviatura',)

class ProductoForm(forms.Form):
    codigo_barras_1 = forms.CharField(max_length=13, label="Código de Barras #1")
    codigo_barras_2 = forms.CharField(max_length=13, label="Código de Barras #2")
    nombre_compra = forms.CharField(max_length=60, label="Nombre de Compra")
    nombre_venta = forms.CharField(max_length=60, label="Nombre de Venta")
    nombre_corto = forms.CharField(max_length=15, label="Nombre Corto")
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoría")
    id_fabricante = forms.ModelChoiceField(queryset=Fabricante.objects.all(), label="Fabricante")
    id_presentacion = forms.ModelChoiceField(queryset=Presentacion.objects.all(), label="Presentación")
    id_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), label="País")
    id_unidad_medida = forms.ModelChoiceField(queryset=Unidad_Medida.objects.all(), label="Unidad de Medida")
    conversion = forms.IntegerField(label = 'Conversión')
    id_via_administracion = forms.ModelChoiceField(queryset=Via_Administracion.objects.all(), label="Vía de Administración")
    prioridad = forms.IntegerField(label='Prioridad')
    #imagen = forms.ImageField(upload_to='media/images', label='Imagen')
    id_tipo_prescripcion = forms.ModelChoiceField(queryset=Tipo_Prescripcion.objects.all(), label="Tipo de Prescripción")
    afecto_impuesto = forms.BooleanField(label='Afecto a Impuestos')
    registro_sanitario = forms.CharField(max_length=20, label="Registro Sanitario")
    precio_costo = forms.DecimalField(max_digits=10, decimal_places=5, label="Precio Costo")
    precio_venta = forms.DecimalField(max_digits=7, decimal_places=2, label="Precio Venta")
    clasificacion_abc = forms.CharField(max_length=1, label="Clasificación ABC")


