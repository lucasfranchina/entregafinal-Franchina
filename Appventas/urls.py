from Appventas import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio),
    path('clientes/', views.clientes),
    path('productos/', views.productos),
    path('servicios/', views.servicios),
]