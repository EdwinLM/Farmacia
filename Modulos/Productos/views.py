from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Modulos.Productos.models import Categoria, Fabricante, Presentacion, Unidad_Medida, Via_Administracion, Tipo_Prescripcion, Componente, Indicacion, Impuesto, Pais

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
    #paginate_by = 2

class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = "__all__"
    success_message = 'Categoria Creada Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class CategoriaDetalle(DetailView):
    model = Categoria

class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    model = Categoria
    form = Categoria
    fields = "__all__"
    success_message = 'Categoria Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria 
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Categoria Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')
 
# ******************
# ** LABORATORIOS **
# ******************

class LaboratoriosListado(ListView):
    model = Fabricante
    #paginate_by = 2

class LaboratorioCrear(SuccessMessageMixin, CreateView):
    model = Fabricante
    form = Fabricante
    fields = "__all__"
    success_message = 'Laboratorio Creado Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class LaboratorioDetalle(DetailView):
    model = Fabricante

class LaboratorioActualizar(SuccessMessageMixin, UpdateView):
    model = Fabricante
    form = Fabricante
    fields = "__all__"
    success_message = 'Laboratorio Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class LaboratorioEliminar(SuccessMessageMixin, DeleteView):
    model = Fabricante 
    form = Fabricante
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Laboratorio Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

# ********************
# ** PRESENTACIONES **
# ********************

class PresentacionesListado(ListView):
    model = Presentacion
    #paginate_by = 2

class PresentacionCrear(SuccessMessageMixin, CreateView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"
    success_message = 'Presentación Creada Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class PresentacionDetalle(DetailView):
    model = Presentacion

class PresentacionActualizar(SuccessMessageMixin, UpdateView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"
    success_message = 'Presentación Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class PresentacionEliminar(SuccessMessageMixin, DeleteView):
    model = Presentacion
    form = Presentacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Presentación Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

# ************************
# ** UNIDADES DE MEDIDA **
# ************************

class UnidadesListado(ListView):
    model = Unidad_Medida
    #paginate_by = 2

class UnidadCrear(SuccessMessageMixin, CreateView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"
    success_message = 'Unidad de Medida Creada Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class UnidadDetalle(DetailView):
    model = Unidad_Medida

class UnidadActualizar(SuccessMessageMixin, UpdateView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"
    success_message = 'Unidad de Medida Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class UnidadEliminar(SuccessMessageMixin, DeleteView):
    model = Unidad_Medida
    form = Unidad_Medida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Unidad de Medida Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

# ****************************
# ** VÍAS DE ADMINISTRACIÓN **
# ****************************

class ViasListado(ListView):
    model = Via_Administracion
    #paginate_by = 2

class ViaCrear(SuccessMessageMixin, CreateView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"
    success_message = 'Vía de Administración Creada Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class ViaDetalle(DetailView):
    model = Via_Administracion

class ViaActualizar(SuccessMessageMixin, UpdateView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"
    success_message = 'Vía de Administración Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class ViaEliminar(SuccessMessageMixin, DeleteView):
    model = Via_Administracion
    form = Via_Administracion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Vía de Administración Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

# ***************************
# ** TIPOS DE PRESCRIPCIÓN **
# ***************************

class PrescripcionesListado(ListView):
    model = Tipo_Prescripcion
    #paginate_by = 2

class PrescripcionCrear(SuccessMessageMixin, CreateView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"
    success_message = 'Tipo de Prescripcion Creado Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class PrescripcionDetalle(DetailView):
    model = Tipo_Prescripcion

class PrescripcionActualizar(SuccessMessageMixin, UpdateView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"
    success_message = 'Tipo de Prescripcion Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class PrescripcionEliminar(SuccessMessageMixin, DeleteView):
    model = Tipo_Prescripcion
    form = Tipo_Prescripcion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Tipo de Prescripcion Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')


# *************************
# ** COMPONENTES ACTIVOS **
# *************************

class ComponentesListado(ListView):
    model = Componente
    #paginate_by = 2

class ComponenteCrear(SuccessMessageMixin, CreateView):
    model = Componente
    form = Componente
    fields = "__all__"
    success_message = 'Componente Activo Creado Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class ComponenteDetalle(DetailView):
    model = Componente

class ComponenteActualizar(SuccessMessageMixin, UpdateView):
    model = Componente
    form = Componente
    fields = "__all__"
    success_message = 'Componente Activo Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class ComponenteEliminar(SuccessMessageMixin, DeleteView):
    model = Componente
    form = Componente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Componente Activo Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

# ******************
# ** INDICACIONES **
# ******************

class IndicacionesListado(ListView):
    model = Indicacion
    #paginate_by = 2

class IndicacionCrear(SuccessMessageMixin, CreateView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"
    success_message = 'Indicación Creada Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class IndicacionDetalle(DetailView):
    model = Indicacion

class IndicacionActualizar(SuccessMessageMixin, UpdateView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"
    success_message = 'Indicación Actualizada Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class IndicacionEliminar(SuccessMessageMixin, DeleteView):
    model = Indicacion
    form = Indicacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Indicación Eliminada Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')


# ***************
# ** IMPUESTOS **
# ***************

class ImpuestosListado(ListView):
    model = Impuesto
    #paginate_by = 2

class ImpuestoCrear(SuccessMessageMixin, CreateView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"
    success_message = 'Impuesto Creado Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class ImpuestoDetalle(DetailView):
    model = Impuesto

class ImpuestoActualizar(SuccessMessageMixin, UpdateView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"
    success_message = 'Impuesto Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class ImpuestoEliminar(SuccessMessageMixin, DeleteView):
    model = Impuesto
    form = Impuesto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Impuesto Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')


# ************
# ** PAISES **
# ************

class PaisesListado(ListView):
    model = Pais
    #paginate_by = 2

class PaisCrear(SuccessMessageMixin, CreateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message = 'Pais Creado Correctamente !'
 
    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leer')

class PaisDetalle(DetailView):
    model = Pais

class PaisActualizar(SuccessMessageMixin, UpdateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message = 'Pais Actualizado Correctamente !'
 
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):
        return reverse('leer')
 
class PaisEliminar(SuccessMessageMixin, DeleteView):
    model = Pais
    form = Pais
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self):
        success_message = 'Pais Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')

