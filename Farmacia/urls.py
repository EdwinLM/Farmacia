"""Farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Modulos.Productos import views
from Modulos.Productos.views import CategoriasListado, CategoriaDetalle, CategoriaCrear, CategoriaActualizar, CategoriaEliminar
from Modulos.Productos.views import LaboratoriosListado, LaboratorioDetalle, LaboratorioCrear, LaboratorioActualizar, LaboratorioEliminar
from Modulos.Productos.views import PresentacionesListado, PresentacionDetalle, PresentacionCrear, PresentacionActualizar, PresentacionEliminar
from Modulos.Productos.views import UnidadesListado, UnidadDetalle, UnidadCrear, UnidadActualizar, UnidadEliminar
from Modulos.Productos.views import ViasListado, ViaDetalle, ViaCrear, ViaActualizar, ViaEliminar
from Modulos.Productos.views import PrescripcionesListado, PrescripcionDetalle, PrescripcionCrear, PrescripcionActualizar, PrescripcionEliminar
from Modulos.Productos.views import ComponentesListado, ComponenteDetalle, ComponenteCrear, ComponenteActualizar, ComponenteEliminar
from Modulos.Productos.views import IndicacionesListado, IndicacionDetalle, IndicacionCrear, IndicacionActualizar, IndicacionEliminar
from Modulos.Productos.views import ImpuestosListado, ImpuestoDetalle, ImpuestoCrear, ImpuestoActualizar, ImpuestoEliminar
from Modulos.Productos.views import PaisesListado, PaisDetalle, PaisCrear, PaisActualizar, PaisEliminar
from Modulos.Productos.views import ProductosListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar

urlpatterns = [
    path('admin/', admin.site.urls),

    path('categorias/', CategoriasListado.as_view(template_name = "categorias/index.html"), name='leer'),
    path('categorias/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "categorias/detalles.html"), name='detalles'),
    path('categorias/crear', CategoriaCrear.as_view(template_name = "categorias/crear.html"), name='crear'),
    path('categorias/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "categorias/actualizar.html"), name='actualizar'), 
    path('categorias/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='eliminar'),

    path('laboratorios/', LaboratoriosListado.as_view(template_name = "laboratorios/index.html"), name='leer'),
    path('laboratorios/detalle/<int:pk>', LaboratorioDetalle.as_view(template_name = "laboratorios/detalles.html"), name='detalles'),
    path('laboratorios/crear', LaboratorioCrear.as_view(template_name = "laboratorios/crear.html"), name='crear'),
    path('laboratorios/editar/<int:pk>', LaboratorioActualizar.as_view(template_name = "laboratorios/actualizar.html"), name='actualizar'), 
    path('laboratorios/eliminar/<int:pk>', LaboratorioEliminar.as_view(), name='eliminar'),

    path('presentaciones/', PresentacionesListado.as_view(template_name = "presentaciones/index.html"), name='leer'),
    path('presentaciones/detalle/<int:pk>', PresentacionDetalle.as_view(template_name = "presentaciones/detalles.html"), name='detalles'),
    path('presentaciones/crear', PresentacionCrear.as_view(template_name = "presentaciones/crear.html"), name='crear'),
    path('presentaciones/editar/<int:pk>', PresentacionActualizar.as_view(template_name = "presentaciones/actualizar.html"), name='actualizar'), 
    path('presentaciones/eliminar/<int:pk>', PresentacionEliminar.as_view(), name='eliminar'),

    path('unidades/', UnidadesListado.as_view(template_name = "unidades/index.html"), name='leer'),
    path('unidades/detalle/<int:pk>', UnidadDetalle.as_view(template_name = "unidades/detalles.html"), name='detalles'),
    path('unidades/crear', UnidadCrear.as_view(template_name = "unidades/crear.html"), name='crear'),
    path('unidades/editar/<int:pk>', UnidadActualizar.as_view(template_name = "unidades/actualizar.html"), name='actualizar'), 
    path('unidades/eliminar/<int:pk>', UnidadEliminar.as_view(), name='eliminar'),

    path('vias/', ViasListado.as_view(template_name = "vias/index.html"), name='leer'),
    path('vias/detalle/<int:pk>', ViaDetalle.as_view(template_name = "vias/detalles.html"), name='detalles'),
    path('vias/crear', ViaCrear.as_view(template_name = "vias/crear.html"), name='crear'),
    path('vias/editar/<int:pk>', ViaActualizar.as_view(template_name = "vias/actualizar.html"), name='actualizar'), 
    path('vias/eliminar/<int:pk>', ViaEliminar.as_view(), name='eliminar'),

    path('prescripciones/', PrescripcionesListado.as_view(template_name = "prescripciones/index.html"), name='leer'),
    path('prescripciones/detalle/<int:pk>', PrescripcionDetalle.as_view(template_name = "prescripciones/detalles.html"), name='detalles'),
    path('prescripciones/crear', PrescripcionCrear.as_view(template_name = "prescripciones/crear.html"), name='crear'),
    path('prescripciones/editar/<int:pk>', PrescripcionActualizar.as_view(template_name = "prescripciones/actualizar.html"), name='actualizar'), 
    path('prescripciones/eliminar/<int:pk>', PrescripcionEliminar.as_view(), name='eliminar'),

    path('componentes/', ComponentesListado.as_view(template_name = "componentes/index.html"), name='leer'),
    path('componentes/detalle/<int:pk>', ComponenteDetalle.as_view(template_name = "componentes/detalles.html"), name='detalles'),
    path('componentes/crear', ComponenteCrear.as_view(template_name = "componentes/crear.html"), name='crear'),
    path('componentes/editar/<int:pk>', ComponenteActualizar.as_view(template_name = "componentes/actualizar.html"), name='actualizar'), 
    path('componentes/eliminar/<int:pk>', ComponenteEliminar.as_view(), name='eliminar'),

    path('indicaciones/', IndicacionesListado.as_view(template_name = "indicaciones/index.html"), name='leer'),
    path('indicaciones/detalle/<int:pk>', IndicacionDetalle.as_view(template_name = "indicaciones/detalles.html"), name='detalles'),
    path('indicaciones/crear', IndicacionCrear.as_view(template_name = "indicaciones/crear.html"), name='crear'),
    path('indicaciones/editar/<int:pk>', IndicacionActualizar.as_view(template_name = "indicaciones/actualizar.html"), name='actualizar'), 
    path('indicaciones/eliminar/<int:pk>', IndicacionEliminar.as_view(), name='eliminar'),

    path('impuestos/', ImpuestosListado.as_view(template_name = "impuestos/index.html"), name='leer'),
    path('impuestos/detalle/<int:pk>', ImpuestoDetalle.as_view(template_name = "impuestos/detalles.html"), name='detalles'),
    path('impuestos/crear', ImpuestoCrear.as_view(template_name = "impuestos/crear.html"), name='crear'),
    path('impuestos/editar/<int:pk>', ImpuestoActualizar.as_view(template_name = "impuestos/actualizar.html"), name='actualizar'), 
    path('impuestos/eliminar/<int:pk>', ImpuestoEliminar.as_view(), name='eliminar'),

    path('paises/', PaisesListado.as_view(template_name = "paises/index.html"), name='leer'),
    path('paises/detalle/<int:pk>', PaisDetalle.as_view(template_name = "paises/detalles.html"), name='detalles'),
    path('paises/crear', PaisCrear.as_view(template_name = "paises/crear.html"), name='crear'),
    path('paises/editar/<int:pk>', PaisActualizar.as_view(template_name = "paises/actualizar.html"), name='actualizar'), 
    path('paises/eliminar/<int:pk>', PaisEliminar.as_view(), name='eliminar'),

    path('productos/', ProductosListado.as_view(template_name = "productos/index.html"), name='leer'),
    path('productos/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detalles'),
    path('productos/crear', views.ProductoCrear, name='crear'),
    path('productos/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='actualizar'), 
    path('productos/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar'),
    
]   
