import datetime
from django.shortcuts import render
from django.db import transaction
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
import json
from django.views.generic import ListView, DetailView 
from django.views.generic import CreateView, UpdateView, DeleteView
from Modulos.Productos.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Unidad_Medida, Via_Administracion, Tipo_Prescripcion, Componente, Indicacion, Impuesto, Pais
from Modulos.Productos.models import Producto, Sucursal, Inventario, Forma_Pago, Tipo_Cliente, Genero, Cliente, Venta, Detalle_Venta

from Modulos.Productos.forms import ProductoForm, VentaForm, ClienteForm, CategoriaForm, FabricanteForm, PresentacionForm, PaisForm
from Modulos.Productos.forms import UnidadMedidaForm, ViaAdministracionForm, TipoPrescripcionForm

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

# ****************
# ** CATEGORIAS **
# ****************

#class CategoriasListado(IsSuperuserMixin, ListView):
class CategoriasListado(ValidatePermissionRequiredMixin, ListView):
    permission_required = 's'
    model = Categoria

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #def post(self, request, *args, **kwargs):
    #    data = {}
    #    try:
    #        action = request.POST['action']
    #        if action == 'searchdata':
    #            data = []
    #            for i in Categoria.objects.all():
    #                data.append(i.toJSON())
    #        else:
    #            data['error'] = 'Ha ocurrido un error'
    #    except Exception as e:
    #        data['error'] = str(e)
    #    return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('crearcat')
        return context

class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = "__all__"
    success_message = 'Categoria Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categorías'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leercat')

class CategoriaDetalle(DetailView):
    model = Categoria

class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    model = Categoria
    form = Categoria
    fields = "__all__"
    success_message = 'Categoria Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leercat')
 
class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria 
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Categoria Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leercat')
 
# ******************
# ** LABORATORIOS **
# ******************

class LaboratoriosListado(ListView):
    model = Fabricante

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Fabricante.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Laboratorios'
        context['create_url'] = reverse_lazy('crearlab')
        return context

class LaboratorioCrear(SuccessMessageMixin, CreateView):
    model = Fabricante
    form = Fabricante
    fields = "__all__"
    success_message = 'Laboratorio Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Laboratorios'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerlab')

class LaboratorioDetalle(DetailView):
    model = Fabricante

class LaboratorioActualizar(SuccessMessageMixin, UpdateView):
    model = Fabricante
    form = Fabricante
    fields = "__all__"
    success_message = 'Laboratorio Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerlab')
 
class LaboratorioEliminar(SuccessMessageMixin, DeleteView):
    model = Fabricante 
    form = Fabricante
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Laboratorio Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerlab')

# ********************
# ** PRESENTACIONES **
# ********************

class PresentacionesListado(ListView):
    model = Presentacion

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Presentacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Presentaciones'
        context['create_url'] = reverse_lazy('crearpre')
        return context

class PresentacionCrear(SuccessMessageMixin, CreateView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"
    success_message = 'Presentación Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Presentaciones'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerpre')

class PresentacionDetalle(DetailView):
    model = Presentacion

class PresentacionActualizar(SuccessMessageMixin, UpdateView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"
    success_message = 'Presentación Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerpre')
 
class PresentacionEliminar(SuccessMessageMixin, DeleteView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Presentación Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerpre')

# ************************
# ** UNIDADES DE MEDIDA **
# ************************

class UnidadesListado(ListView):
    model = Unidad_Medida

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Unidad_Medida.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Unidades de Medida'
        context['create_url'] = reverse_lazy('crearuni')
        return context

class UnidadCrear(SuccessMessageMixin, CreateView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"
    success_message = 'Unidad de Medida Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Unidades de Medida'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leeruni')

class UnidadDetalle(DetailView):
    model = Unidad_Medida

class UnidadActualizar(SuccessMessageMixin, UpdateView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"
    success_message = 'Unidad de Medida Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leeruni')
 
class UnidadEliminar(SuccessMessageMixin, DeleteView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Unidad de Medida Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leeruni')

# ****************************
# ** VÍAS DE ADMINISTRACIÓN **
# ****************************

class ViasListado(ListView):
    model = Via_Administracion

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Via_Administracion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Vias de Administración'
        context['create_url'] = reverse_lazy('crearvia')
        return context

class ViaCrear(SuccessMessageMixin, CreateView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"
    success_message = 'Vía de Administración Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Vias de Administración'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leervia')

class ViaDetalle(DetailView):
    model = Via_Administracion

class ViaActualizar(SuccessMessageMixin, UpdateView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"
    success_message = 'Vía de Administración Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leervia')
 
class ViaEliminar(SuccessMessageMixin, DeleteView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Vía de Administración Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leervia')

# ***************************
# ** TIPOS DE PRESCRIPCIÓN **
# ***************************

class PrescripcionesListado(ListView):
    model = Tipo_Prescripcion

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Tipo_Prescripcion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipos de Prescripción'
        context['create_url'] = reverse_lazy('crearprr')
        return context
    
class PrescripcionCrear(SuccessMessageMixin, CreateView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"
    success_message = 'Tipo de Prescripcion Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Tipos de Prescripción'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerprr')

class PrescripcionDetalle(DetailView):
    model = Tipo_Prescripcion

class PrescripcionActualizar(SuccessMessageMixin, UpdateView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"
    success_message = 'Tipo de Prescripcion Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerprr')
 
class PrescripcionEliminar(SuccessMessageMixin, DeleteView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Tipo de Prescripcion Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerprr')


# *************************
# ** COMPONENTES ACTIVOS **
# *************************

class ComponentesListado(ListView):
    model = Componente

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Componente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Componentes'
        context['create_url'] = reverse_lazy('crearcom')
        return context

class ComponenteCrear(SuccessMessageMixin, CreateView):
    model = Componente
    form = Componente
    fields = "__all__"
    success_message = 'Componente Activo Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Componentes Activos'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leercom')

class ComponenteDetalle(DetailView):
    model = Componente

class ComponenteActualizar(SuccessMessageMixin, UpdateView):
    model = Componente
    form = Componente
    fields = "__all__"
    success_message = 'Componente Activo Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leercom')
 
class ComponenteEliminar(SuccessMessageMixin, DeleteView):
    model = Componente
    form = Componente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Componente Activo Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leercom')

# ******************
# ** INDICACIONES **
# ******************

class IndicacionesListado(ListView):
    model = Indicacion

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Indicacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Indicaciones'
        context['create_url'] = reverse_lazy('crearind')
        return context

class IndicacionCrear(SuccessMessageMixin, CreateView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"
    success_message = 'Indicación Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Indicaciones'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerind')

class IndicacionDetalle(DetailView):
    model = Indicacion

class IndicacionActualizar(SuccessMessageMixin, UpdateView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"
    success_message = 'Indicación Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerind')
 
class IndicacionEliminar(SuccessMessageMixin, DeleteView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Indicación Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerind')


# ***************
# ** IMPUESTOS **
# ***************

class ImpuestosListado(ListView):
    model = Impuesto

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Impuesto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Impuestos'
        context['create_url'] = reverse_lazy('crearimp')
        return context

class ImpuestoCrear(SuccessMessageMixin, CreateView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"
    success_message = 'Impuesto Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Impuestos'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerimp')

class ImpuestoDetalle(DetailView):
    model = Impuesto

class ImpuestoActualizar(SuccessMessageMixin, UpdateView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"
    success_message = 'Impuesto Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerimp')
 
class ImpuestoEliminar(SuccessMessageMixin, DeleteView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Impuesto Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerimp')


# ************
# ** PAISES **
# ************

class PaisesListado(ListView):
    model = Pais

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Pais.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Paises'
        context['create_url'] = reverse_lazy('crearpai')
        return context

class PaisCrear(SuccessMessageMixin, CreateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message = 'Pais Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Paises'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerpai')

class PaisDetalle(DetailView):
    model = Pais

class PaisActualizar(SuccessMessageMixin, UpdateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message = 'Pais Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerpai')
 
class PaisEliminar(SuccessMessageMixin, DeleteView):
    model = Pais
    form = Pais
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Pais Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerpai')


# ***************
# ** PRODUCTOS **
# ***************

class ProductosListado(ListView):
    model = Producto

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #def post(self, request, *args, **kwargs):
    #    data = {}
    #    try:
    #        action = request.GET['action']
    #        if action == 'searchdata':
    #            data = []
    #            for i in Producto.objects.all():
    #                data.append(i)
    #        else:
    #            data['error'] = 'Ha ocurrido un error'
    #    except Exception as e:
    #        data['error'] = str(e)
    #    return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('crearpro')
        context['list_url'] = reverse_lazy('leerpro')
        context['entity'] = 'Producto'
        return context

class ProductoCrear(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/crear.html'
    success_message = 'Producto Creado Correctamente!'
    success_url = reverse_lazy('leerpro')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    form = self.get_form()
                    data = form.save()
                    data = {}
                    data['exito'] = 1
                    #product = Producto()
                    #product.codigo_barras_1 = form.cleaned_data['codigo_barras_1']
                    #product.codigo_barras_2 = form.cleaned_data['codigo_barras_2']
                    #product.nombre_compra = form.cleaned_data['nombre_compra']
                    #product.nombre_venta = form.cleaned_data['nombre_venta']
                    #product.nombre_corto = form.cleaned_data['nombre_corto']
                    #product.id_categoria = form.cleaned_data['id_categoria']
                    #product.id_fabricante = form.cleaned_data['id_fabricante']
                    #product.id_presentacion = form.cleaned_data['id_presentacion']
                    #product.id_pais = form.cleaned_data['id_pais']
                    #product.id_unidad_medida = form.cleaned_data['id_unidad_medida']
                    #product.conversion = form.cleaned_data['conversion']
                    #product.id_via_administracion = form.cleaned_data['id_via_administracion']
                    #product.prioridad = form.cleaned_data['prioridad']
                    #product.imagen = form.cleaned_data['imagen']
                    #product.id_tipo_prescripcion = form.cleaned_data['id_tipo_prescripcion']
                    #product.afecto_impuesto = form.cleaned_data['afecto_impuesto']
                    #product.registro_sanitario = form.cleaned_data['registro_sanitario']
                    #product.precio_costo = form.cleaned_data['precio_costo']
                    #product.precio_venta = form.cleaned_data['precio_venta']
                    #product.clasificacion_abc = form.cleaned_data['clasificacion_abc']
                    #product.estado = 'A'
                    #product.id_empresa = 1
                    #product.save()

                #CREAR PRODUCTO EN TABLA DE INVENTARIO EN CEDIS Y SUCURSALES
            elif action == 'create_categoria':
                with transaction.atomic():
                    frmCategoria = CategoriaForm(request.POST)
                    data = frmCategoria.save()
            elif action == 'create_fabricante':
                with transaction.atomic():
                    frmFabricante = FabricanteForm(request.POST)
                    data = frmFabricante.save()
            elif action == 'create_presentacion':
                with transaction.atomic():
                    frmPresentacion = PresentacionForm(request.POST)
                    data = frmPresentacion.save()
            elif action == 'create_pais':
                with transaction.atomic():
                    frmPais = PaisForm(request.POST)
                    data = frmPais.save()
            elif action == 'create_unidad':
                with transaction.atomic():
                    frmMedida = UnidadMedidaForm(request.POST)
                    data = frmMedida.save()
            elif action == 'create_via':
                with transaction.atomic():
                    frmVia = ViaAdministracionForm(request.POST)
                    data = frmVia.save()
            elif action == 'create_prescripcion':
                with transaction.atomic():
                    frmPrescripcion = TipoPrescripcionForm(request.POST)
                    data = frmPrescripcion.save()
            else:
                data['error'] = 'No se ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Productos'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('leerpro')
        context['action'] = 'add'
        context['frmCategoria'] = CategoriaForm()
        context['frmFabricante'] = FabricanteForm()
        context['frmPresentacion'] = PresentacionForm()
        context['frmPais'] = PaisForm()
        context['frmMedida'] = UnidadMedidaForm()
        context['frmVia'] = ViaAdministracionForm()
        context['frmPrescripcion'] = TipoPrescripcionForm()
        return context


    # Redireccionamos a la página principal luego de crear un registro o categoria
    #def get_success_url(self):
    #    return reverse('leerpro')



def ProductoCrear2(request):
    form = ProductoForm()
    success_message = 'Producto Creado Correctamente !'
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print("Valido")
            product = Producto()
            product.codigo_barras_1 = form.cleaned_data['codigo_barras_1']
            product.codigo_barras_2 = form.cleaned_data['codigo_barras_2']
            product.nombre_compra = form.cleaned_data['nombre_compra']
            product.nombre_venta = form.cleaned_data['nombre_venta']
            product.nombre_corto = form.cleaned_data['nombre_corto']
            product.id_categoria = form.cleaned_data['id_categoria']
            product.id_fabricante = form.cleaned_data['id_fabricante']
            product.id_presentacion = form.cleaned_data['id_presentacion']
            product.id_pais = form.cleaned_data['id_pais']
            product.id_unidad_medida = form.cleaned_data['id_unidad_medida']
            product.conversion = form.cleaned_data['conversion']
            product.id_via_administracion = form.cleaned_data['id_via_administracion']
            product.prioridad = form.cleaned_data['prioridad']
            #product.imagen = form.cleaned_data['imagen']
            product.id_tipo_prescripcion = form.cleaned_data['id_tipo_prescripcion']
            product.afecto_impuesto = form.cleaned_data['afecto_impuesto']
            product.registro_sanitario = form.cleaned_data['registro_sanitario']
            product.precio_costo = form.cleaned_data['precio_costo']
            product.precio_venta = form.cleaned_data['precio_venta']
            product.clasificacion_abc = form.cleaned_data['clasificacion_abc']
            product.estado = 'A'
            product.id_empresa = 1
            product.save()

            #CREAR PRODUCTO EN TABLA DE INVENTARIO EN CEDIS Y SUCURSALES


            return reverse('leerpro')
        else:
            print("Invalido")

    return render(request, 'productos/crear.html', { 'form' : form })
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    #def get_success_url(self):
    #    return reverse('leerpro')

class ProductoDetalle(DetailView):
    model = Producto

class ProductoActualizar(SuccessMessageMixin, UpdateView):
    model = Producto
    form = Producto
    fields = "__all__"
    success_message = 'Producto Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerpro')
 
class ProductoEliminar(SuccessMessageMixin, DeleteView):
    model = Producto
    form = Producto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Producto Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerpro')


# *****************************
# ** CENTROS DE DISTRIBUCION **
# *****************************

class CedisListado(ListView):
    model = Sucursal

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Sucursal.objects.filter(tipo='C')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sucursal.objects.filter(tipo='C'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Centros de Distribución'
        context['create_url'] = reverse_lazy('crearced')
        return context

class CedisCrear(SuccessMessageMixin, CreateView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"
    success_message = 'Centro de Distribución Creado Correctamente !'
    success_url = reverse_lazy('leerced')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    suc = Sucursal()
                    suc.descripcion = request.POST['descripcion']
                    suc.direccion = request.POST['direccion']
                    suc.telefono = request.POST['telefono']
                    suc.abreviatura = request.POST['abreviatura']
                    suc.encargado = request.POST['encargado']
                    suc.email = request.POST['email']
                    suc.tipo = request.POST['tipo']
                    suc.estado = request.POST['estado']
                    suc.id_empresa = int(request.POST['id_empresa'])
                    suc.save()
                    for p in Producto.objects.all():
                        i = Inventario()
                        i.id_sucursal = suc
                        i.id_producto = p
                        i.existencia = 0
                        i.ubicacion = ""
                        i.id_empresa = 1
                        i.save()
                    data = {'id': suc.id_sucursal}

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Centros de Distribución'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('leerced')
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerced')

class CedisDetalle(DetailView):
    model = Sucursal

class CedisActualizar(SuccessMessageMixin, UpdateView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"
    success_message = 'Centro de Distribución Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerced')
 
class CedisEliminar(SuccessMessageMixin, DeleteView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Centro de Distribución Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerced')


# ****************
# ** SUCURSALES **
# ****************

class SucursalListado(ListView):
    model = Sucursal

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Sucursal.objects.filter(tipo='S')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sucursal.objects.filter(tipo='S'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Sucursales'
        context['create_url'] = reverse_lazy('crearsuc')
        return context

class SucursalCrear(SuccessMessageMixin, CreateView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"
    success_message = 'Sucursal Creada Correctamente !'
    success_url = reverse_lazy('leersuc')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    suc = Sucursal()
                    suc.descripcion = request.POST['descripcion']
                    suc.direccion = request.POST['direccion']
                    suc.telefono = request.POST['telefono']
                    suc.abreviatura = request.POST['abreviatura']
                    suc.encargado = request.POST['encargado']
                    suc.email = request.POST['email']
                    suc.tipo = request.POST['tipo']
                    suc.estado = request.POST['estado']
                    suc.id_empresa = int(request.POST['id_empresa'])
                    suc.save()
                    for p in Producto.objects.all():
                        i = Inventario()
                        i.id_sucursal = suc
                        i.id_producto = p
                        i.existencia = 0
                        i.ubicacion = ""
                        i.id_empresa = 1
                        i.save()
                    data = {'id': suc.id_sucursal}

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Sucursales'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('leersuc')
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leersuc')

class SucursalDetalle(DetailView):
    model = Sucursal

class SucursalActualizar(SuccessMessageMixin, UpdateView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"
    success_message = 'Sucursal Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leersuc')
 
class SucursalEliminar(SuccessMessageMixin, DeleteView):
    model = Sucursal
    form = Sucursal
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Sucursal Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leersuc')


# ********************
# ** FORMAS DE PAGO **
# ********************

class FormasPagoListado(ListView):
    model = Forma_Pago

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Pais.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Formas de Pago'
        context['create_url'] = reverse_lazy('crearfp')
        return context

class FormasPagoCrear(SuccessMessageMixin, CreateView):
    model = Forma_Pago
    form = Forma_Pago
    fields = "__all__"
    success_message = 'Forma de Pago Creada Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Formas de Pago'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerfp')

class FormasPagoDetalle(DetailView):
    model = Forma_Pago

class FormasPagoActualizar(SuccessMessageMixin, UpdateView):
    model = Forma_Pago
    form = Forma_Pago
    fields = "__all__"
    success_message = 'Forma de Pago Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leerfp')
 
class FormasPagoEliminar(SuccessMessageMixin, DeleteView):
    model = Forma_Pago
    form = Forma_Pago
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Forma de Pago Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leerfp')


# *************
# ** GÉNEROS **
# *************

class GenerosListado(ListView):
    model = Genero

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Genero.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Géneros'
        context['create_url'] = reverse_lazy('creargen')
        return context

class GenerosCrear(SuccessMessageMixin, CreateView):
    model = Genero
    form = Genero
    fields = "__all__"
    success_message = 'Género Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Géneros'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leergen')

class GenerosDetalle(DetailView):
    model = Genero

class GenerosActualizar(SuccessMessageMixin, UpdateView):
    model = Genero
    form = Genero
    fields = "__all__"
    success_message = 'Género Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leergen')
 
class GenerosEliminar(SuccessMessageMixin, DeleteView):
    model = Genero
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Género Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leergen')


# ***********************
# ** TIPOS DE CLIENTES **
# ***********************

class TiposClientesListado(ListView):
    model = Tipo_Cliente

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Tipo_Cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipos de Clientes'
        context['create_url'] = reverse_lazy('creartc')
        return context

class TiposClientesCrear(SuccessMessageMixin, CreateView):
    model = Tipo_Cliente
    form = Tipo_Cliente
    fields = "__all__"
    success_message = 'Tipo de Clientes Creado Correctamente !'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Tipos de Clientes'
        return context
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leertc')

class TiposClientesDetalle(DetailView):
    model = Tipo_Cliente

class TiposClientesActualizar(SuccessMessageMixin, UpdateView):
    model = Tipo_Cliente
    form = Tipo_Cliente
    fields = "__all__"
    success_message = 'Tipo de Clientes Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leertc')
 
class TiposClientesEliminar(SuccessMessageMixin, DeleteView):
    model = Tipo_Cliente
    form = Tipo_Cliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Tipo de Clientes Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leertc')


# **************
# ** CLIENTES **
# **************

class ClientesListado(ListView):
    model = Cliente

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('crearcli')
        return context

class ClientesCrear(SuccessMessageMixin, CreateView):
    model = Cliente
    form = Cliente
    #fields = ('nombre', 'nit', 'telefono', 'direccion', 'genero', 'nacimiento', 'id_tipo_cliente')
    success_message = 'Cliente Creado Correctamente !'

    form_class = ClienteForm
    template_name = 'clientes/crear.html'
    success_url = reverse_lazy('leercli')
    #permission_required = 'add_client'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leercli')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Cliente'
        context['entity'] = 'Cliente'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class ClientesDetalle(DetailView):
    model = Cliente

class ClientesActualizar(SuccessMessageMixin, UpdateView):
    model = Cliente
    form = Cliente
    fields = ('nombre', 'nit', 'telefono', 'direccion', 'genero', 'nacimiento', 'id_tipo_cliente')
    success_message = 'Cliente Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leercli')
 
class ClientesEliminar(SuccessMessageMixin, DeleteView):
    model = Cliente
    form = Cliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Cliente Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leercli')


# ************
# ** VENTAS **
# ************

class VentaCrear(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/crear.html'
    success_url = reverse_lazy('crearvta')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term'].strip()
                #products = Product.objects.filter(stock__gt=0)
                products = Producto.objects.all()
                if len(term):
                    products = products.filter(nombre_venta__icontains=term)
                for i in products.exclude(id_producto__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['value'] = i.nombre_venta
                    # item['text'] = i.name
                    data.append(item)
            elif action == 'search_autocomplete':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term'].strip()
                #term = request.POST['term']
                data.append({'id': term, 'text': term})
                #products = Product.objects.filter(name__icontains=term, stock__gt=0)
                products = Producto.objects.filter(nombre_venta__icontains=term)
                for i in products.exclude(id_producto__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['id'] = i.id_producto
                    item['text'] = i.nombre_venta
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sucur = Sucursal.objects.filter(id_sucursal=vents['id_sucursal']).first()
                    clien = Cliente.objects.filter(id_cliente=vents['id_cliente']).first()
                    venta = Venta()
                    venta.id_sucursal = sucur
                    #venta.fecha = vents['fecha']
                    venta.fecha = datetime.datetime.now() 
                    venta.id_cliente = clien
                    venta.nombre = vents['nombre']
                    venta.nit = vents['nit']
                    venta.telefono = vents['telefono']
                    venta.direccion = vents['direccion']
                    venta.subtotal_afecto = vents['subtotal_afecto']
                    venta.subtotal_noafecto = vents['subtotal_noafecto']
                    venta.iva = vents['iva']
                    venta.total = vents['total']
                    venta.id_empresa = 1
                    venta.vendedor = 1
                    venta.cajero = 1
                    venta.correlativo_diario = 1
                    venta.id_forma_pago = Forma_Pago.objects.filter(id_forma_pago=vents['id_forma_pago']).first()
                    venta.save()
                    for i in vents['products']:
                        p = Producto.objects.filter(id_producto=i['id_producto']).first()
                        detalle = Detalle_Venta()
                        detalle.id_venta = venta
                        detalle.id_producto = p
                        detalle.cantidad = i['cant']
                        detalle.id_empresa = 1
                        detalle.precio_costo = p.precio_costo
                        detalle.precio_venta = p.precio_venta
                        detalle.save()
                    data = {'id': venta.id_venta}
            elif action == 'buscar_clientes':
                data = []
                term = request.POST['term']
                clients = Cliente.objects.filter(nombre__icontains=term)
                    #Q(names__icontains=term) | Q(surnames__icontains=term) | Q(dni__icontains=term))[0:10]
                    #Q(nombre__icontains=term))[0:10]

                for i in clients:
                    item = i.toJSON()
                    item['id'] = i.id_cliente
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_client':
                with transaction.atomic():
                    frmClient = ClienteForm(request.POST)
                    data = frmClient.save()
            else:
                data['error'] = 'No se ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Venta'
        context['entity'] = 'Venta'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        context['frmClient'] = ClienteForm()
        return context
