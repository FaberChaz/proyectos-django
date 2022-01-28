from django.contrib import admin
from gestionpedidos.models import Clientes, Articulo, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellidos', 'telefono')
    search_fields=('nombre', 'apellidos', 'telefono')

class ProductosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'seccion', 'precio')
    search_fields=('nombre', 'seccion')
    list_filter=('seccion',)

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha', 'entregado')
    search_fields=('numero', 'fecha')
    list_filter=('numero', 'fecha')
    date_hierarchy='fecha'



admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulo, ProductosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
