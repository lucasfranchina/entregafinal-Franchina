from Appventas import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
    #path('clientes-form/', views.clientes_form, name='clientesform'),
    path('clientes-form2/', views.clientes_form2, name='clientesform2'),
    path('productos-form2/', views.productos_form2, name='productosform2'),
    path('servicios-form2/', views.servicios_form2, name='serviciosform2'),
]