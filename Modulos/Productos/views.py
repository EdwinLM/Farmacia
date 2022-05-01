from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic import CreateView, UpdateView, DeleteView
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Unidad_Medida, Via_Administracion, Tipo_Prescripcion, Componente, Indicacion, Impuesto, Pais, Producto

from Modulos.Productos.forms import ProductoForm

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

class CategoriasListado(ListView):
    model = Categoria
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context

class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = "__all__"
    success_message = 'Categoria Creada Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Laboratorios'
        return context

class LaboratorioCrear(SuccessMessageMixin, CreateView):
    model = Fabricante
    form = Fabricante
    fields = "__all__"
    success_message = 'Laboratorio Creado Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Presentaciones'
        return context

class PresentacionCrear(SuccessMessageMixin, CreateView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"
    success_message = 'Presentación Creada Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Unidades de Medida'
        return context

class UnidadCrear(SuccessMessageMixin, CreateView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"
    success_message = 'Unidad de Medida Creada Correctamente !'
 
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

    @method_decorator(login_required)
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Prescripciones'
        return context

class PrescripcionCrear(SuccessMessageMixin, CreateView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"
    success_message = 'Tipo de Prescripcion Creado Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Componentes Activos'
        return context

class ComponenteCrear(SuccessMessageMixin, CreateView):
    model = Componente
    form = Componente
    fields = "__all__"
    success_message = 'Componente Activo Creado Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Indicaciones'
        return context

class IndicacionCrear(SuccessMessageMixin, CreateView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"
    success_message = 'Indicación Creada Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Impuestos'
        return context

class ImpuestoCrear(SuccessMessageMixin, CreateView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"
    success_message = 'Impuesto Creado Correctamente !'
 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Paises'
        return context

class PaisCrear(SuccessMessageMixin, CreateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message = 'Pais Creado Correctamente !'
 
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

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #def post(self, request, *args, **kwargs):
    #    data = {}
    #    try:
    #        action = request.POST['action']
    #        if action == 'add':
    #            form = self.get_form()
    #            data = form.save()
    #        else:
    #            data['error'] = 'No ha ingresado a ninguna acción'
    #    except Exception as e:
    #        data['error'] = str(e)
    #    return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Productos'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('leerpro')
        context['action'] = 'add'
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


