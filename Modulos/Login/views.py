from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.shortcuts import redirect

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