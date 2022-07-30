from django.contrib.auth import update_session_auth_hash
from datetime import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, TemplateView, PasswordResetView
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView 
from django.views.generic import CreateView, UpdateView, DeleteView, View, FormView
from Modulos.Productos.mixins import ValidatePermissionRequiredMixin
from Modulos.Login.models import User
from Modulos.Productos.forms import UserForm, UserProfileForm
from Modulos.Productos.models import Empresa
from random import randint

#class UserListado(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
class UserListado(ListView):
	model = User
	template_name = 'usuarios/'
	permission_required = 'user.view_user'

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
				for i in User.objects.all():
					data.append(i.toJSON())
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Usuarios'
		context['create_url'] = reverse_lazy('crearusr')
		context['action'] = 'searchdata'
		context['empresa'] = Empresa.objects.first().nombre
		return context

class UsuarioCrear(CreateView):
    model = User
    #form = User
    form_class = UserForm
    #fields = "__all__"
    success_message = 'Usuario Creado Correctamente !'
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('leerusr')
    #permission_required = 'add_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerusr')

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
        context['title'] = 'Creación de Usuarios'
        context['entity'] = 'User'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['empresa'] = Empresa.objects.first().nombre
        return context

class UsuarioActualizar(UpdateView):
    model = User
    #form = User
    form_class = UserForm
    #fields = "__all__"
    success_message = 'Usuario Actualizado Correctamente !'
    template_name = 'usuarios/crear.html'
    success_url = reverse_lazy('leerusr')
    #permission_required = 'change_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
    	self.object = self.get_object()
    	return super().dispatch(request, *args, **kwargs)

    # Redireccionamos a la página principal luego de crear un registro o categoria
    def get_success_url(self):
        return reverse('leerusr')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                #data['error'] = 'No ha ingresado a ninguna opción'
                data['error'] = action
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Usuarios'
        context['entity'] = 'User'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['empresa'] = Empresa.objects.first().nombre
        return context

class UsuarioEliminar(DeleteView):
	model = User
	template_name = 'usuarios/eliminar.html'
	success_url = reverse_lazy('leerusr')
	#permission_required = 'delete_user'
	url_redirect = success_url

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			self.object.delete()
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminación de un Usuario'
		context['entity'] = 'User'
		context['list_url'] = self.success_url
		context['empresa'] = Empresa.objects.first().nombre
		return context

class UsuarioCambiarGrupo(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		try:
			print(self.kwargs)
			request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
		except:
			pass
		return HttpResponseRedirect(reverse_lazy('dashboard'))

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'usuarios/profile.html'
    success_url = reverse_lazy('dashboard')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Perfil'
        context['entity'] = 'Perfil'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['empresa'] = Empresa.objects.first().nombre
        return context

class UserChangePasswordView(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'usuarios/change_password.html'
    success_url = reverse_lazy('login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        form.fields['old_password'].widget.attrs['placeholder'] = 'Ingrese su contraseña actual'
        form.fields['new_password1'].widget.attrs['placeholder'] = 'Ingrese su nueva contraseña'
        form.fields['new_password2'].widget.attrs['placeholder'] = 'Repita su contraseña nueva'
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Password'
        context['entity'] = 'Password'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['empresa'] = Empresa.objects.first().nombre
        return context

class LoginFormView(LoginView):
	template_name = 'usuarios/login.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('dashboard')
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Iniciar Sesión'
		context['empresa'] = Empresa.objects.first().nombre
		return context

class DashboardView(TemplateView):
	template_name = 'dashboard.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		request.user.get_group_session()
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'get_graph_sales_year_month':
				data = {
					'name': 'Porcentaje de venta',
					'showInLegend': False,
					'colorByPoint': True,
					'data': self.get_graph_sales_year_month()
				}
			elif action == 'get_graph_sales_products_year_month':
				data = {
					'name': 'Porcentaje',
					'colorByPoint': True,
					'data': self.get_graph_sales_products_year_month(),
				}
			elif action == 'get_graph_online':
				data = {'y': randint(1, 100)}
				print(data)
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_graph_sales_year_month(self):
		data = []
		try:
			year = datetime.now().year
			for m in range(1, 13):
				total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(
					r=Coalesce(Sum('total'), 0)).get('r')
				data.append(float(total))
		except:
			pass
		return data

	def get_graph_sales_products_year_month(self):
		data = []
		year = datetime.now().year
		month = datetime.now().month
		try:
			for p in Product.objects.all():
				total = DetSale.objects.filter(sale__date_joined__year=year, sale__date_joined__month=month,
												prod_id=p.id).aggregate(
					r=Coalesce(Sum('subtotal'), 0)).get('r')
				if total > 0:
					data.append({
						'name': p.name,
						'y': float(total)
					})
		except:
			pass
		return data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['panel'] = 'Panel de administrador'
		context['graph_sales_year_month'] = self.get_graph_sales_year_month()
		context['empresa'] = Empresa.objects.first().nombre
		return context


class DashboardCajeroView(TemplateView):
	template_name = 'dashboardcaj.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		request.user.get_group_session()
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'get_graph_sales_year_month':
				data = {
					'name': 'Porcentaje de venta',
					'showInLegend': False,
					'colorByPoint': True,
					'data': self.get_graph_sales_year_month()
				}
			elif action == 'get_graph_sales_products_year_month':
				data = {
					'name': 'Porcentaje',
					'colorByPoint': True,
					'data': self.get_graph_sales_products_year_month(),
				}
			elif action == 'get_graph_online':
				data = {'y': randint(1, 100)}
				print(data)
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_graph_sales_year_month(self):
		data = []
		try:
			year = datetime.now().year
			for m in range(1, 13):
				total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(
					r=Coalesce(Sum('total'), 0)).get('r')
				data.append(float(total))
		except:
			pass
		return data

	def get_graph_sales_products_year_month(self):
		data = []
		year = datetime.now().year
		month = datetime.now().month
		try:
			for p in Product.objects.all():
				total = DetSale.objects.filter(sale__date_joined__year=year, sale__date_joined__month=month,
												prod_id=p.id).aggregate(
					r=Coalesce(Sum('subtotal'), 0)).get('r')
				if total > 0:
					data.append({
						'name': p.name,
						'y': float(total)
					})
		except:
			pass
		return data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['panel'] = 'Panel de administrador'
		context['graph_sales_year_month'] = self.get_graph_sales_year_month()
		context['empresa'] = Empresa.objects.first().nombre
		return context


class OpcionView(TemplateView):
	template_name = 'opcion.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		request.user.get_group_session()
		return super().get(request, *args, **kwargs)

