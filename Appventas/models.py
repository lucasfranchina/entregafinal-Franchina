from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Productos(models.Model):
    producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.producto} - {self.marca}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Servicios(models.Model):
    servicio = models.CharField(max_length=30)
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.servicio} - {self.proveedor}"
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

