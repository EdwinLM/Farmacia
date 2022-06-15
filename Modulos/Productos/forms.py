from datetime import datetime
from django.forms import *
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Pais, Unidad_Medida, Via_Administracion, Tipo_Prescripcion, Producto, Cliente, Venta

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Categoria
        fields = ('descripcion',)
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class FabricanteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Fabricante
        fields = ('nombre',)
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class PresentacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Presentacion
        fields = ('descripcion',)
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class PaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Pais
        fields = ('nombre',)
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class UnidadMedidaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Unidad_Medida
        fields = ('descripcion',)
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ViaAdministracionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Via_Administracion
        fields = ('descripcion',)
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TipoPrescripcionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Tipo_Prescripcion
        fields = ('descripcion',)
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'abreviatura': TextInput(
                attrs={
                    'placeholder': 'Ingrese una abreviatura',
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


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
        self.fields['clasificacion_abc'].label = 'x'
        self.fields['clasificacion_abc'].widget.attrs['hidden'] = True
        self.fields['estado'].label = 'x'
        self.fields['estado'].widget.attrs['hidden'] = True
        self.fields['id_empresa'].label = 'x'
        self.fields['id_empresa'].widget.attrs['hidden'] = True
        self.fields['id_categoria'].label = 'Categoría'
        self.fields['id_fabricante'].label = 'Fabricante'
        self.fields['id_presentacion'].label = 'Presentación'
        self.fields['id_pais'].label = 'País'
        self.fields['id_unidad_medida'].label = 'Unidad de Medida'
        self.fields['id_via_administracion'].label = 'Vía de Administración'
        self.fields['id_tipo_prescripcion'].label = 'Tipo de Prescripción'


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


class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_cliente'].queryset = Cliente.objects.none()

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'id_cliente': Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'fecha': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha',
                    'data-target': '#fecha',
                    'data-toggle': 'datetimepicker'
            }),
            'nit': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'nombre': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'telefono': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'direccion': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'subtotal_afecto': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'subtotal_noafecto': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'iva': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
        }


class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = ('nombre', 'nit', 'telefono', 'direccion', 'genero', 'nacimiento', 'id_tipo_cliente')
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre completo',
                    'autofocus': True,
                    'class': 'form-control',
                }
            ),
            'nit': TextInput(
                attrs={
                    'placeholder': 'Ingrese su NIT',
                    'class': 'form-control',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese su telefono',
                    'class': 'form-control',
                }
            ),
            'nacimiento': DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
                    'class': 'form-control',
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                    'class': 'form-control',
                }
            ),
            'genero': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_tipo_cliente': Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
