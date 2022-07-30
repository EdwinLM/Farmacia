from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView
from Modulos.Productos.forms import ReporteVentaForm
from Modulos.Productos.models import Venta, Empresa
from django.db.models.functions import Coalesce
from django.db.models import Sum

# Create your views here.
class ReporteVentaView(TemplateView):
	template_name = 'rpt/rptventa.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'search_rptventa':
				data = []
				start_date = request.POST.get('start_date', '')
				end_date = request.POST.get('end_date', '')
				sucur = request.POST['id_sucursal']
				search = Venta.objects.all().filter(id_sucursal=sucur)
				if len(start_date) and len(end_date):
					print(start_date, '   ', end_date)
					search = search.filter(fecha__range=[start_date, end_date])
				for s in search:
					data.append([
						s.id_venta,
						s.id_sucursal.abreviatura,
						s.id_cliente.nombre,
						s.fecha.strftime('%d-%m-%Y %H:%M:%S'),
						format(s.total, '.2f')
					])
				total = search.aggregate(r=Sum('total'))['r'] or 0
				data.append([
						'---',
						'---',
						'---',
						'---',
						format(total, '.2f')
					])
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de Ventas'
		context['list_url'] = reverse_lazy('dashboard')
		context['form'] = ReporteVentaForm()
		context['empresa'] = Empresa.objects.first().nombre
		return context




class ReporteVentaCajeroView(TemplateView):
	template_name = 'cajero/rptventa.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'search_rptventa':
				data = []
				start_date = request.POST.get('start_date', '')
				end_date = request.POST.get('end_date', '')
				sucur = request.POST['id_sucursal']
				search = Venta.objects.all().filter(id_sucursal=sucur)
				if len(start_date) and len(end_date):
					print(start_date, '   ', end_date)
					search = search.filter(fecha__range=[start_date, end_date])
				for s in search:
					data.append([
						s.id_venta,
						s.id_sucursal.abreviatura,
						s.id_cliente.nombre,
						s.fecha.strftime('%d-%m-%Y %H:%M:%S'),
						format(s.total, '.2f')
					])
				total = search.aggregate(r=Sum('total'))['r'] or 0
				data.append([
						'---',
						'---',
						'---',
						'---',
						format(total, '.2f')
					])
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de Ventas'
		context['list_url'] = reverse_lazy('dashboardcaj')
		context['form'] = ReporteVentaForm()
		context['empresa'] = Empresa.objects.first().nombre
		return context

