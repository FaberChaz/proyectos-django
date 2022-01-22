import email
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return 'Nombre: %s, Apellido: %s, Direccion: %s, Email: %s, Telefono: %s' %(self.nombre, self.apellidos, self.direccion, self.email, self.telefono)

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return 'Nombre producto: %s, Seccion: %s, Precio: %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    