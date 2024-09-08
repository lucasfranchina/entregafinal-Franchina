from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Appventas.models import Clientes, Productos, Servicios
from Appventas.forms import ClientesFormulario, ProductosFormulario, ServiciosFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(req):
    return render(req, 'appventas/padre.html')

def about(req):
    fecha_actual = datetime.now()
    return render(req, 'appventas/about.html', {'fecha_actual': fecha_actual})

def clientes(req):
    return render(req, 'appventas/clientes.html')

def productos(req):
    return render(req, 'appventas/productos.html')

def servicios(req):
    return render(req, 'appventas/servicios.html')

class clienteslistview(ListView):
    model = Clientes
    template_name = 'appventas/clientes.html'

class clientesdetalle(DetailView):
    model = Clientes
    template_name = 'appventas/clientesdetalle.html'

class clientescreateview(CreateView):
    model = Clientes
    template_name = 'appventas/clientesform.html'
    success_url = reverse_lazy('listaclientes')
    fields = ['nombre', 'apellido', 'direccion', 'email']

class clientesupdateview(UpdateView):
    model = Clientes
    template_name = 'appventas/clientesedit.html'
    success_url = reverse_lazy('listaclientes')
    fields = ['nombre', 'apellido', 'direccion', 'email']

class clientesdeleteview(DeleteView):
    model = Clientes
    template_name = 'appventas/clientesdelete.html'
    success_url = reverse_lazy('listaclientes')


class productoslistview(ListView):
    model = Productos
    template_name = 'appventas/productos.html'

class productosdetalle(DetailView):
    model = Productos
    template_name = 'appventas/productosdetalle.html'

class productoscreateview(CreateView):
    model = Productos
    template_name = 'appventas/productosform.html'
    success_url = reverse_lazy('listaproductos')
    fields = ['producto', 'marca', 'precio']

class productosupdateview(UpdateView):
    model = Productos
    template_name = 'appventas/productosedit.html'
    success_url = reverse_lazy('listaproductos')
    fields = ['producto', 'marca', 'precio']

class productosdeleteview(DeleteView):
    model = Productos
    template_name = 'appventas/productosdelete.html'
    success_url = reverse_lazy('listaproductos')


class servicioslistview(ListView):
    model = Servicios
    template_name = 'appventas/servicios.html'

class serviciosdetalle(DetailView):
    model = Servicios
    template_name = 'appventas/serviciosdetalle.html'

class servicioscreateview(CreateView):
    model = Servicios
    template_name = 'appventas/serviciosform.html'
    success_url = reverse_lazy('listaservicios')
    fields = ['servicio', 'precio', 'proveedor']

class serviciosupdateview(UpdateView):
    model = Servicios
    template_name = 'appventas/serviciosedit.html'
    success_url = reverse_lazy('listaservicios')
    fields = ['servicio', 'precio', 'proveedor']

class serviciosdeleteview(DeleteView):
    model = Servicios
    template_name = 'appventas/serviciosdelete.html'
    success_url = reverse_lazy('listaservicios')

def busquedaproductos(req):
    return render (req, 'appventas/busquedaproductos.html')

def buscar(req):
    if req.GET['producto']:
        producto = req.GET['producto']
        productos2 = Productos.objects.filter(producto__contains=producto)

        return render(req, "appventas/busquedaproductos.html", {"productos2":productos2, "producto": producto})
    
    else:
        respuesta = "No se enviaron datos"
    
    return render(req, "appventas/busquedaproductos.html", {"respuesta":respuesta})