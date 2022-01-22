from django.contrib import admin
from gestionpedidos.models import Clientes, Articulo, Pedidos
# Register your models here.

admin.site.register(Clientes)
admin.site.register(Articulo)
admin.site.register(Pedidos)
