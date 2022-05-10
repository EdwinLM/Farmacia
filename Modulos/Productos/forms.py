from django.forms import *
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Pais, Unidad_Medida, Via_Administracion, Tipo_Prescripcion, Producto

class CategoriaForm(forms.Form):
    #descripcion = forms.CharField(max_length=30, help_text = "Enter a name")

    class Meta:
        model = Categoria
        fields = ('descripcion','abreviatura',)

class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo_barras_1'].widget.attrs['autofocus'] = True
        self.fields['codigo_barras_1'].label = 'Código de Barras para Compras'
        self.fields['codigo_barras_1'].widget.attrs['placeholder'] = 'Ingrese el código de barras para compras'
        self.fields['codigo_barras_2'].label = 'Código de Barras para Ventas'
        self.fields['codigo_barras_2'].widget.attrs['placeholder'] = 'Ingrese el código de barras para ventas'
        self.fields['nombre_compra'].widget.attrs['placeholder'] = 'Ingrese la descripción para compras'
        self.fields['nombre_venta'].widget.attrs['placeholder'] = 'Ingrese la descripción para ventas'
        self.fields['nombre_corto'].widget.attrs['placeholder'] = 'Ingrese la descripción corta para ventas'
        self.fields['registro_sanitario'].widget.attrs['placeholder'] = 'Ingrese el registro sanitario'
        self.fields['precio_costo'].widget.attrs['placeholder'] = 'Ingrese el precio costo'
        self.fields['precio_venta'].widget.attrs['placeholder'] = 'Ingrese el precio venta'
        self.fields['clasificacion_abc'].label = ''
        self.fields['clasificacion_abc'].widget.attrs['hidden'] = True
        self.fields['estado'].label = ''
        self.fields['estado'].widget.attrs['hidden'] = True
        self.fields['id_empresa'].label = ''
        self.fields['id_empresa'].widget.attrs['hidden'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        #widgets = {
        #    'nombre_compra': TextInput(
        #        attrs={
        #            'placeholder': 'Ingrese el nombre de compras',
        #        }
        #    ),
        #}

    #codigo_barras_1 = forms.CharField(max_length=13, label="Código de Barras Compras")
    #codigo_barras_2 = forms.CharField(max_length=13, label="Código de Barras Ventas")
    #nombre_compra = forms.CharField(max_length=60, label="Nombre de Compra")
    #nombre_venta = forms.CharField(max_length=60, label="Nombre de Venta")
    #nombre_corto = forms.CharField(max_length=15, label="Nombre Corto")
    #id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoría")
    #id_fabricante = forms.ModelChoiceField(queryset=Fabricante.objects.all(), label="Fabricante")
    #id_presentacion = forms.ModelChoiceField(queryset=Presentacion.objects.all(), label="Presentación")
    #id_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), label="País")
    #id_unidad_medida = forms.ModelChoiceField(queryset=Unidad_Medida.objects.all(), label="Unidad de Medida")
    #conversion = forms.IntegerField(label = 'Conversión')
    #id_via_administracion = forms.ModelChoiceField(queryset=Via_Administracion.objects.all(), label="Vía de Administración")
    #prioridad = forms.IntegerField(label='Prioridad')
    #imagen = forms.ImageField(upload_to='product/%Y/%m/%d', label='Imagen')
    #id_tipo_prescripcion = forms.ModelChoiceField(queryset=Tipo_Prescripcion.objects.all(), label="Tipo de Prescripción")
    #afecto_impuesto = forms.BooleanField(label='Afecto a Impuestos', required=False)
    #registro_sanitario = forms.CharField(max_length=20, label="Registro Sanitario")
    #precio_costo = forms.DecimalField(max_digits=10, decimal_places=5, label="Precio Costo")
    #precio_venta = forms.DecimalField(max_digits=7, decimal_places=2, label="Precio Venta")
    #clasificacion_abc = forms.CharField(max_length=1, label="Clasificación ABC")

