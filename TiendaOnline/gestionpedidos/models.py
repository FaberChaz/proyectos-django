import email
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    