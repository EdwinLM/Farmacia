from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView 
from django.views.generic import CreateView, UpdateView, DeleteView
from Modulos.Productos.mixins import ValidatePermissionRequiredMixin
from Modulos.Login.models import User

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
		#context['create_url'] = reverse_lazy('crearusr')
		return context




class LoginFormView(LoginView):
	template_name = 'login.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('leervia')
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Iniciar Sesión'
		return context

class DashboardView(TemplateView):
	template_name = 'dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(kwargs)
		context['panel'] = 'Panel de Administrador'
		return context
