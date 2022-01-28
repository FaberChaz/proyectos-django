import email
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La direccion")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
