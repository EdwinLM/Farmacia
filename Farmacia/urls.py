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
from django.conf import settings
from django.conf.urls.static import static

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
from Modulos.Productos.views import CedisListado, CedisDetalle, CedisCrear, CedisActualizar, CedisEliminar
from Modulos.Productos.views import SucursalListado, SucursalDetalle, SucursalCrear, SucursalActualizar, SucursalEliminar
from Modulos.Productos.views import FormasPagoListado, FormasPagoDetalle, FormasPagoCrear, FormasPagoActualizar, FormasPagoEliminar
from Modulos.Productos.views import TiposClientesListado, TiposClientesDetalle, TiposClientesCrear, TiposClientesActualizar, TiposClientesEliminar
from Modulos.Productos.views import ClientesListado, ClientesDetalle, ClientesCrear, ClientesActualizar, ClientesEliminar
from Modulos.Productos.views import GenerosListado, GenerosDetalle, GenerosCrear, GenerosActualizar, GenerosEliminar
from Modulos.Productos.views import VentaCrear
from Modulos.Login.views import UserListado, UsuarioCrear, UsuarioActualizar, UsuarioEliminar, UsuarioCambiarGrupo, UserProfileView, UserChangePasswordView, LoginFormView, LogoutView, DashboardView
from reportes.views import ReporteVentaView
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('usuarios/', UserListado.as_view(template_name = "usuarios/index.html"), name='leerusr'),
    path('usuarios/crear', UsuarioCrear.as_view(template_name = "usuarios/crear.html"), name='crearusr'),
    path('usuarios/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "usuarios/crear.html"), name='actualizarusr'), 
    path('usuarios/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='eliminarusr'),
    path('usuarios/cambiar/grupo/<int:pk>', UsuarioCambiarGrupo.as_view(), name='cambiargrupousr'),
    path('usuarios/profile/', UserProfileView.as_view(), name='profileusr'),
    path('usuarios/change_password/', UserChangePasswordView.as_view(), name='changepasswordusr'),

    path('categorias/', CategoriasListado.as_view(template_name = "categorias/index.html"), name='leercat'),
    path('categorias/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "categorias/detalles.html"), name='detallescat'),
    path('categorias/crear', CategoriaCrear.as_view(template_name = "categorias/crear.html"), name='crearcat'),
    path('categorias/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "categorias/actualizar.html"), name='actualizarcat'), 
    path('categorias/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='eliminarcat'),

    path('laboratorios/', LaboratoriosListado.as_view(template_name = "laboratorios/index.html"), name='leerlab'),
    path('laboratorios/detalle/<int:pk>', LaboratorioDetalle.as_view(template_name = "laboratorios/detalles.html"), name='detalleslab'),
    path('laboratorios/crear', LaboratorioCrear.as_view(template_name = "laboratorios/crear.html"), name='crearlab'),
    path('laboratorios/editar/<int:pk>', LaboratorioActualizar.as_view(template_name = "laboratorios/actualizar.html"), name='actualizarlab'), 
    path('laboratorios/eliminar/<int:pk>', LaboratorioEliminar.as_view(), name='eliminarlab'),

    path('presentaciones/', PresentacionesListado.as_view(template_name = "presentaciones/index.html"), name='leerpre'),
    path('presentaciones/detalle/<int:pk>', PresentacionDetalle.as_view(template_name = "presentaciones/detalles.html"), name='detallespre'),
    path('presentaciones/crear', PresentacionCrear.as_view(template_name = "presentaciones/crear.html"), name='crearpre'),
    path('presentaciones/editar/<int:pk>', PresentacionActualizar.as_view(template_name = "presentaciones/actualizar.html"), name='actualizarpre'), 
    path('presentaciones/eliminar/<int:pk>', PresentacionEliminar.as_view(), name='eliminarpre'),

    path('unidades/', UnidadesListado.as_view(template_name = "unidades/index.html"), name='leeruni'),
    path('unidades/detalle/<int:pk>', UnidadDetalle.as_view(template_name = "unidades/detalles.html"), name='detallesuni'),
    path('unidades/crear', UnidadCrear.as_view(template_name = "unidades/crear.html"), name='crearuni'),
    path('unidades/editar/<int:pk>', UnidadActualizar.as_view(template_name = "unidades/actualizar.html"), name='actualizaruni'), 
    path('unidades/eliminar/<int:pk>', UnidadEliminar.as_view(), name='eliminaruni'),

    path('vias/', ViasListado.as_view(template_name = "vias/index.html"), name='leervia'),
    path('vias/detalle/<int:pk>', ViaDetalle.as_view(template_name = "vias/detalles.html"), name='detallesvia'),
    path('vias/crear', ViaCrear.as_view(template_name = "vias/crear.html"), name='crearvia'),
    path('vias/editar/<int:pk>', ViaActualizar.as_view(template_name = "vias/actualizar.html"), name='actualizarvia'), 
    path('vias/eliminar/<int:pk>', ViaEliminar.as_view(), name='eliminarvia'),

    path('prescripciones/', PrescripcionesListado.as_view(template_name = "prescripciones/index.html"), name='leerprr'),
    path('prescripciones/detalle/<int:pk>', PrescripcionDetalle.as_view(template_name = "prescripciones/detalles.html"), name='detallesprr'),
    path('prescripciones/crear', PrescripcionCrear.as_view(template_name = "prescripciones/crear.html"), name='crearprr'),
    path('prescripciones/editar/<int:pk>', PrescripcionActualizar.as_view(template_name = "prescripciones/actualizar.html"), name='actualizarprr'), 
    path('prescripciones/eliminar/<int:pk>', PrescripcionEliminar.as_view(), name='eliminarprr'),

    path('componentes/', ComponentesListado.as_view(template_name = "componentes/index.html"), name='leercom'),
    path('componentes/detalle/<int:pk>', ComponenteDetalle.as_view(template_name = "componentes/detalles.html"), name='detallescom'),
    path('componentes/crear', ComponenteCrear.as_view(template_name = "componentes/crear.html"), name='crearcom'),
    path('componentes/editar/<int:pk>', ComponenteActualizar.as_view(template_name = "componentes/actualizar.html"), name='actualizarcom'), 
    path('componentes/eliminar/<int:pk>', ComponenteEliminar.as_view(), name='eliminarcom'),

    path('indicaciones/', IndicacionesListado.as_view(template_name = "indicaciones/index.html"), name='leerind'),
    path('indicaciones/detalle/<int:pk>', IndicacionDetalle.as_view(template_name = "indicaciones/detalles.html"), name='detallesind'),
    path('indicaciones/crear', IndicacionCrear.as_view(template_name = "indicaciones/crear.html"), name='crearind'),
    path('indicaciones/editar/<int:pk>', IndicacionActualizar.as_view(template_name = "indicaciones/actualizar.html"), name='actualizarind'), 
    path('indicaciones/eliminar/<int:pk>', IndicacionEliminar.as_view(), name='eliminarind'),

    path('impuestos/', ImpuestosListado.as_view(template_name = "impuestos/index.html"), name='leerimp'),
    path('impuestos/detalle/<int:pk>', ImpuestoDetalle.as_view(template_name = "impuestos/detalles.html"), name='detallesimp'),
    path('impuestos/crear', ImpuestoCrear.as_view(template_name = "impuestos/crear.html"), name='crearimp'),
    path('impuestos/editar/<int:pk>', ImpuestoActualizar.as_view(template_name = "impuestos/actualizar.html"), name='actualizarimp'), 
    path('impuestos/eliminar/<int:pk>', ImpuestoEliminar.as_view(), name='eliminarimp'),

    path('paises/', PaisesListado.as_view(template_name = "paises/index.html"), name='leerpai'),
    path('paises/detalle/<int:pk>', PaisDetalle.as_view(template_name = "paises/detalles.html"), name='detallespai'),
    path('paises/crear', PaisCrear.as_view(template_name = "paises/crear.html"), name='crearpai'),
    path('paises/editar/<int:pk>', PaisActualizar.as_view(template_name = "paises/actualizar.html"), name='actualizarpai'), 
    path('paises/eliminar/<int:pk>', PaisEliminar.as_view(), name='eliminarpai'),

    path('productos/', ProductosListado.as_view(template_name = "productos/index.html"), name='leerpro'),
    path('productos/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detallespro'),
    path('productos/crear', ProductoCrear.as_view(template_name = "productos/crear.html"), name='crearpro'),
    path('productos/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='actualizarpro'), 
    path('productos/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminarpro'),

    path('cedis/', CedisListado.as_view(template_name = "cedis/index.html"), name='leerced'),
    path('cedis/detalle/<int:pk>', CedisDetalle.as_view(template_name = "cedis/detalles.html"), name='detallesced'),
    path('cedis/crear', CedisCrear.as_view(template_name = "cedis/crear.html"), name='crearced'),
    path('cedis/editar/<int:pk>', CedisActualizar.as_view(template_name = "cedis/actualizar.html"), name='actualizarced'),
    path('cedis/eliminar/<int:pk>', CedisEliminar.as_view(), name='eliminarced'),

    path('sucursales/', SucursalListado.as_view(template_name = "sucursales/index.html"), name='leersuc'),
    path('sucursales/detalle/<int:pk>', SucursalDetalle.as_view(template_name = "sucursales/detalles.html"), name='detallessuc'),
    path('sucursales/crear', SucursalCrear.as_view(template_name = "sucursales/crear.html"), name='crearsuc'),
    path('sucursales/editar/<int:pk>', SucursalActualizar.as_view(template_name = "sucursales/actualizar.html"), name='actualizarsuc'),
    path('sucursales/eliminar/<int:pk>', SucursalEliminar.as_view(), name='eliminarsuc'),

    path('formaspago/', FormasPagoListado.as_view(template_name = "formaspago/index.html"), name='leerfp'),
    path('formaspago/detalle/<int:pk>', FormasPagoDetalle.as_view(template_name = "formaspago/detalles.html"), name='detallesfp'),
    path('formaspago/crear', FormasPagoCrear.as_view(template_name = "formaspago/crear.html"), name='crearfp'),
    path('formaspago/editar/<int:pk>', FormasPagoActualizar.as_view(template_name = "formaspago/actualizar.html"), name='actualizarfp'),
    path('formaspago/eliminar/<int:pk>', FormasPagoEliminar.as_view(), name='eliminarfp'),

    path('generos/', GenerosListado.as_view(template_name = "generos/index.html"), name='leergen'),
    path('generos/detalle/<int:pk>', GenerosDetalle.as_view(template_name = "generos/detalles.html"), name='detallesgen'),
    path('generos/crear', GenerosCrear.as_view(template_name = "generos/crear.html"), name='creargen'),
    path('generos/editar/<int:pk>', GenerosActualizar.as_view(template_name = "generos/actualizar.html"), name='actualizargen'),
    path('generos/eliminar/<int:pk>', GenerosEliminar.as_view(), name='eliminargen'),

    path('tipoclientes/', TiposClientesListado.as_view(template_name = "tipoclientes/index.html"), name='leertc'),
    path('tipoclientes/detalle/<int:pk>', TiposClientesDetalle.as_view(template_name = "tipoclientes/detalles.html"), name='detallestc'),
    path('tipoclientes/crear', TiposClientesCrear.as_view(template_name = "tipoclientes/crear.html"), name='creartc'),
    path('tipoclientes/editar/<int:pk>', TiposClientesActualizar.as_view(template_name = "tipoclientes/actualizar.html"), name='actualizartc'),
    path('tipoclientes/eliminar/<int:pk>', TiposClientesEliminar.as_view(), name='eliminartc'),

    path('clientes/', ClientesListado.as_view(template_name = "clientes/index.html"), name='leercli'),
    path('clientes/detalle/<int:pk>', ClientesDetalle.as_view(template_name = "clientes/detalles.html"), name='detallescli'),
    path('clientes/crear', ClientesCrear.as_view(template_name = "clientes/crear.html"), name='crearcli'),
    path('clientes/editar/<int:pk>', ClientesActualizar.as_view(template_name = "clientes/actualizar.html"), name='actualizarcli'),
    path('clientes/eliminar/<int:pk>', ClientesEliminar.as_view(), name='eliminarcli'),

    path('ventas/crear', VentaCrear.as_view(template_name = "ventas/crear.html"), name='crearvta'),

    path('rpt/rptventa', ReporteVentaView.as_view(template_name = "rpt/rptventa.html"), name='rptventa'),
    
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('productos/crear', views.ProductoCrear, name='crearpro'),

