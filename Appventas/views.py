from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Appventas.models import Clientes, Productos, Servicios
from Appventas.forms import ClientesFormulario, ProductosFormulario, ServiciosFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(req):
    return render(req, 'appventas/padre.html')

def about(req):
    fecha_actual = datetime.now()
    return render(req, 'appventas/about.html', {'fecha_actual': fecha_actual})

@login_required
def clientes(req):
    return render(req, 'appventas/clientes.html')

@login_required
def productos(req):
    return render(req, 'appventas/productos.html')

@login_required
def servicios(req):
    return render(req, 'appventas/servicios.html')

class clienteslistview(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'appventas/clientes.html'

class clientesdetalle(LoginRequiredMixin, DetailView):
    model = Clientes
    template_name = 'appventas/clientesdetalle.html'

class clientescreateview(LoginRequiredMixin, CreateView):
    model = Clientes
    template_name = 'appventas/clientesform.html'
    success_url = reverse_lazy('listaclientes')
    fields = ['nombre', 'apellido', 'direccion', 'email']

class clientesupdateview(LoginRequiredMixin, UpdateView):
    model = Clientes
    template_name = 'appventas/clientesedit.html'
    success_url = reverse_lazy('listaclientes')
    fields = ['nombre', 'apellido', 'direccion', 'email']

class clientesdeleteview(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = 'appventas/clientesdelete.html'
    success_url = reverse_lazy('listaclientes')


class productoslistview(LoginRequiredMixin, ListView):
    model = Productos
    template_name = 'appventas/productos.html'

class productosdetalle(LoginRequiredMixin, DetailView):
    model = Productos
    template_name = 'appventas/productosdetalle.html'

class productoscreateview(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = 'appventas/productosform.html'
    success_url = reverse_lazy('listaproductos')
    fields = ['producto', 'marca', 'precio']

class productosupdateview(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'appventas/productosedit.html'
    success_url = reverse_lazy('listaproductos')
    fields = ['producto', 'marca', 'precio']

class productosdeleteview(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'appventas/productosdelete.html'
    success_url = reverse_lazy('listaproductos')


class servicioslistview(LoginRequiredMixin, ListView):
    model = Servicios
    template_name = 'appventas/servicios.html'

class serviciosdetalle(LoginRequiredMixin, DetailView):
    model = Servicios
    template_name = 'appventas/serviciosdetalle.html'

class servicioscreateview(LoginRequiredMixin, CreateView):
    model = Servicios
    template_name = 'appventas/serviciosform.html'
    success_url = reverse_lazy('listaservicios')
    fields = ['servicio', 'precio', 'proveedor']

class serviciosupdateview(LoginRequiredMixin, UpdateView):
    model = Servicios
    template_name = 'appventas/serviciosedit.html'
    success_url = reverse_lazy('listaservicios')
    fields = ['servicio', 'precio', 'proveedor']

class serviciosdeleteview(LoginRequiredMixin, DeleteView):
    model = Servicios
    template_name = 'appventas/serviciosdelete.html'
    success_url = reverse_lazy('listaservicios')

# def busquedaproductos(req):
#     return render (req, 'appventas/busquedaproductos.html')

# def buscar(req):
#     if req.GET['producto']:
#         producto = req.GET['producto']
#         productos2 = Productos.objects.filter(producto__contains=producto)

#         return render(req, "appventas/busquedaproductos.html", {"productos2":productos2, "producto": producto})
    
#     else:
#         respuesta = "No se enviaron datos"
    
#     return render(req, "appventas/busquedaproductos.html", {"respuesta":respuesta})