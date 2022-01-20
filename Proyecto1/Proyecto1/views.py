from django import http
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request): 

    p1 = Persona("faber", "hincapie")

    fecha_actual = datetime.datetime.now()
    temas = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    #doc_externo = get_template('miplantilla.html') #carga la plantilla gracias al loader.get_template
    #documento = doc_externo.render({"nombre_alumno": p1.nombre, "apellido_alumno": p1.apellido, "ahora": fecha_actual, 'temas': temas}) #renderizamos el diccionario,
    return render(request, "miplantilla.html",  {"nombre_alumno": p1.nombre, "apellido_alumno": p1.apellido, "ahora": fecha_actual, 'temas': temas}) #imprime el documento

def despedida(request):
    return HttpResponse("prueba despedida: Nos Vemos")

def demo_fecha(request):#nos da la fecha actual
    fecha_actual = datetime.datetime.now()
    return HttpResponse(f"Fecha y hora actual es {fecha_actual}")

def calcula_edad(request, edad, agno):#recibe dos parametros y calcula la eddad.
    #edadActual = 33
    periodo = agno - 2021
    edadFutura = edad + periodo
    documento = 'Tienes %s años. En el año %s tendrás %s años' %(edad, agno, edadFutura)
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoC.html", {"damefecha": fecha_actual})

def cursoBlog(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoBlog.html", {"damefecha": fecha_actual})
