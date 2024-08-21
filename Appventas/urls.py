from Appventas import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
]