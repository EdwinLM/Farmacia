from django.conf.urls import url
from Modulos.Productos import views

urlpatterns = [
    url(r'^$', views.categorias, name='categorias'),
    url(r'^$', views.laboratorios, name='laboratorios'),
    url(r'^$', views.presentaciones, name='presentaciones'),
    url(r'^$', views.unidades, name='unidades'),
    url(r'^$', views.vias, name='vias'),
    url(r'^$', views.prescripciones, name='prescripciones'),
    url(r'^$', views.componentes, name='componentes'),
    url(r'^$', views.indicaciones, name='indicaciones'),
    url(r'^$', views.impuestos, name='impuestos'),
    url(r'^$', views.paises, name='paises'),
    url(r'^$', views.productos, name='productos'),
    url(r'^$', views.cedis, name='cedis'),
    url(r'^$', views.sucursales, name='sucursales'),
]
