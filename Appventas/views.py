from django.shortcuts import render
from django.http import HttpResponse
from Appventas.models import Clientes, Productos, Servicios
from Appventas.forms import ClientesFormulario, ProductosFormulario, ServiciosFormulario

def inicio(req):
    return render(req, 'appventas/padre.html')

def clientes(req):
    return render(req, 'appventas/clientes.html')

def productos(req):
    return render(req, 'appventas/productos.html')

def servicios(req):
    return render(req, 'appventas/servicios.html')

#def clientes_form(req):
#   if req.method == 'POST':
#      clientes = Clientes(nombre=req.POST['nombre'], apellido=req.POST['apellido'], direccion=req.POST['direccion'], email=req.POST['email'])
#     clientes.save()
#    return render(req, 'appventas/padre.html')
#return render(req, 'appventas/clientesformulario.html')

def clientes_form2(req):
    if req.method == 'POST':
        miformulario = ClientesFormulario(req.POST)
        print(miformulario)

        if miformulario.is_valid:
            información = miformulario.cleaned_data
            clientes = Clientes(nombre=req.POST['nombre'], apellido=req.POST['apellido'], direccion=req.POST['direccion'], email=req.POST['email'])
            clientes.save()
            return render(req, 'appventas/clientes.html')
    else:
        miformulario = ClientesFormulario()
    
    return render(req, 'appventas/clientesformulario2.html', {'miformulario': miformulario})

def productos_form2(req):
    if req.method == 'POST':
        miformulario = ProductosFormulario(req.POST)
        print(miformulario)

        if miformulario.is_valid:
            información = miformulario.cleaned_data
            productos = Productos(producto=req.POST['producto'], marca=req.POST['marca'], precio=req.POST['precio'])
            productos.save()
            return render(req, 'appventas/productos.html')
    else:
        miformulario = ProductosFormulario()
    
    return render(req, 'appventas/productosformulario.html', {'miformulario': miformulario})

def servicios_form2(req):
    if req.method == 'POST':
        miformulario = ServiciosFormulario(req.POST)
        print(miformulario)

        if miformulario.is_valid:
            información = miformulario.cleaned_data
            productos = Servicios(servicio=req.POST['servicio'], precio=req.POST['precio'], proveedor=req.POST['proveedor'])
            productos.save()
            return render(req, 'appventas/servicios.html')
    else:
        miformulario = ServiciosFormulario()
    
    return render(req, 'appventas/serviciosformulario.html', {'miformulario': miformulario})

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