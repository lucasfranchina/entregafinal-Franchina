from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=100)
    email = forms.EmailField()

class ProductosFormulario(forms.Form):
    producto = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class ServiciosFormulario(forms.Form):
    servicio = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    proveedor = forms.CharField(max_length=30)