from django.shortcuts import render
from django.views.generic import TemplateView
from Modulos.Productos.forms import ReporteVentaForm

# Create your views here.
class ReporteVentaView(TemplateView):
	template_name = 'rpt/rptventa.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de Ventas'
		context['list_url'] = 'dashboard'
		context['form'] = ReporteVentaForm()
		return context



