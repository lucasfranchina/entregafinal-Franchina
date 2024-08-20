from django.shortcuts import render
from django.http import HttpResponse

def inicio(req):
    return render(req, 'appventas/index.html')

def clientes(req):
    return render(req, 'appventas/clientes.html')

def productos(req):
    return render(req, 'appventas/productos.html')

def servicios(req):
    return render(req, 'appventas/servicios.html')