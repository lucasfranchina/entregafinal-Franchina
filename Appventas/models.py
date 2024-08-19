from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

class Productos(models.Model):
    producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()

class Servicios(models.Model):
    servicio = models.CharField(max_length=30)
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=30)

