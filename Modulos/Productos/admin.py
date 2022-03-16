from django.contrib import admin
from Modulos.Productos.models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Fabricante)
admin.site.register(Presentacion)
admin.site.register(Pais)
admin.site.register(Unidad_Medida)
admin.site.register(Via_Administracion)
admin.site.register(Tipo_Prescripcion)
admin.site.register(Componente)
admin.site.register(Impuesto)
admin.site.register(Indicacion)
admin.site.register(Producto)
admin.site.register(Producto_Componente)
admin.site.register(Producto_Impuesto)
admin.site.register(Producto_Indicacion)


