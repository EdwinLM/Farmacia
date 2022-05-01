from django.db import models
from django.forms import model_to_dict
from Farmacia.settings import MEDIA_URL, STATIC_URL

# *******************************************************
# ** CLASES PARA MANEJO DE LOS PRODUCTOS EN EL SISTEMA **
# *******************************************************

class Categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30, null=False, blank=False, help_text="Ingrese la descripción de la categoría")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Fabricante(models.Model):
	id_fabricante = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese el nombre del fabricante")
	abreviatura = models.CharField(max_length=5, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = [ "nombre" ]


class Presentacion(models.Model): #Formas Farmaceuticas
	id_presentacion = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese la descripción de la presentación (tabletas, jarabe, etc.)")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Pais(models.Model): #Paises
	id_pais = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese el nombre del país")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = [ "nombre" ]


class Unidad_Medida(models.Model):
	id_unidad_medida = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30, null=False, blank=False, help_text="Ingrese la descripción de la unidad de medida (caja, frasco, botella, etc.)")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Via_Administracion(models.Model): #Vias de Administración
	id_via_administracion = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=100, null=False, blank=False, unique=True, help_text="Ingrese la descripción de la vía de administración (oral, tópica, vaginal, etc.)")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	def toJSON(self):
		item = model_to_dict(self)
		return item

	class Meta:
		ordering = [ "descripcion" ]


class Tipo_Prescripcion(models.Model): #Tipo de Prescripción
	id_tipo_prescripcion = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30, null=False, blank=False, help_text="Ingrese la descripción del tipo de prescripción")
	abreviatura = models.CharField(max_length=5, null=False, blank=False, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Componente(models.Model): #Principios Activos
	id_componente = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=150, null=False, blank=False, help_text="Ingrese la descripción descripción del ingrediente activo")
	abreviatura = models.CharField(max_length=15, help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Impuesto(models.Model): #Impuestos
	id_impuesto = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30, null=False, blank=False, help_text="Ingrese la descripción del impuesto")
	porcentaje = models.DecimalField(max_digits=5, null=False, blank=False, decimal_places=3, help_text="Ingrese la abreviatura a utilizar")
	abreviatura = models.CharField(max_length=10, default='', help_text="Ingrese la abreviatura a utilizar")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Indicacion(models.Model):
	id_indicacion = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese la descripción de la indicación")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	#abreviatura = models.CharField(max_length=5, help_text="Ingrese la abreviatura a utilizar")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.descripcion

	class Meta:
		ordering = [ "descripcion" ]


class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	codigo_barras_1 = models.CharField(max_length=13, help_text="Ingrese el código de barras")
	codigo_barras_2 = models.CharField(max_length=13, help_text="Ingrese el código de barras secundario")
	nombre_compra = models.CharField(max_length=60, null=False, blank=False, help_text="Ingrese el nombre para efectos de compras")
	nombre_venta = models.CharField(max_length=60, null=False, blank=False, help_text="Ingrese el nombre para efectos de ventas")
	nombre_corto = models.CharField(max_length=15, help_text="Ingrese el nombre corto para facturación")
	id_categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione la categoría a la que pertenece")
	id_fabricante = models.ForeignKey(Fabricante, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el fabricante del producto")
	id_presentacion = models.ForeignKey(Presentacion, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione la presentación del producto")
	id_pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el país de origen del producto")
	id_unidad_medida = models.ForeignKey(Unidad_Medida, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione la unidad de medida del proeducto")
	conversion = models.PositiveIntegerField(null=False, blank=False, default=1, help_text = 'Ingrese la conversión del producto en sucursales')
	id_via_administracion = models.ForeignKey(Via_Administracion, null=False, blank=False, on_delete=models.CASCADE, help_text="Ingrese ")
	prioridad = models.PositiveIntegerField(default=3, null=False, blank=False, help_text='Ingrese la prioridad del producto')
	imagen = models.ImageField(upload_to='product/%Y/%m/%d', help_text='Seleccione la imagen del producto', null=True, blank=True)
	id_tipo_prescripcion = models.ForeignKey(Tipo_Prescripcion, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione las prescripciones del producto")
	afecto_impuesto = models.BooleanField(default=False, help_text='Marque si el producto es afecto a impuestos')
	registro_sanitario = models.CharField(max_length=20, help_text="Ingrese el registro sanitario del producto")
	precio_costo = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=5, help_text="Ingrese el precio costo del producto")
	precio_venta = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, help_text="Ingrese el precio de venta del producto")
	clasificacion_abc = models.CharField(max_length=1, default='C', help_text="Ingrese la clasificación ABC a la que pertenece el producto")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.nombre_venta

	def get_image(self):
		if self.imagen:
			return '{}{}'.format(MEDIA_URL, self.imagen)
		return '{}{}'.format(MEDIA_URL, 'images/empty.png')

	def toJSON(self):
		item = model_to_dict(self)
		return item

	class Meta:
		ordering = [ "nombre_venta" ]


class Producto_Componente(models.Model):
	id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el producto")
	id_componente = models.ForeignKey(Componente, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el ingrediente activo del producto")
	cantidad = models.CharField(max_length=20, help_text="Ingrese la cantidad de ingrediente activo en el producto")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

class Producto_Impuesto(models.Model):
	id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el producto")
	id_impuesto = models.ForeignKey(Impuesto, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el impuesto al que está afecto el producto")
	porcentaje = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=3, help_text="Ingrese el porcentaje de impuesto")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)

class Producto_Indicacion(models.Model):
	id_producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione el producto")
	id_indicacion = models.ForeignKey(Indicacion, null=False, blank=False, on_delete=models.CASCADE, help_text="Seleccione la indicación para la que sirve el producto")
	dosis = models.CharField(max_length=20, help_text="Ingrese la dosis del producto")
	estado = models.CharField(max_length=1, default='A', help_text="Ingrese el estado")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	id_empresa = models.PositiveIntegerField(default=1)


# *******************************************************
# ** CLASES PARA MANEJO DE LOS PRODUCTOS EN EL SISTEMA **
# *******************************************************


