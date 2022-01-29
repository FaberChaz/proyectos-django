from django.http import HttpResponse
from django.shortcuts import render
from gestionpedidos.models import Articulo

# Create your views here.

def busqueda_producto(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET['producto']:
    
        #mensaje='Articulo buscado: %r' %request.GET['producto']
        prd = request.GET['producto']

        articulos = Articulo.objects.filter(nombre__icontains=prd)

        return render(request, 'resultados_busqueda.html', {'articulos':articulos, 'query':prd})

    else:
    
        mensaje = 'No has introducido nada'    
    
    return HttpResponse(mensaje)
    
