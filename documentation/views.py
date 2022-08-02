from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    try:
        ramas = Rama.objects.all()
    except Rama.DoesNotExist:
        raise Http404("La rama no existe")

    context = {
        'ramas': ramas
    }

    return render(
        request,
        'documentation/index.html',
        context)

# TODO: Revisar el modelo porque no tiene mucho sentido. 
# Hacer la gestión de todo la rama aquí. 
def rama_documentation(request, rama_name):
    # Search rama by its name
    try:
        rama = Rama.objects.get(nombre__iexact=rama_name)
        trimestres = Trimestre.objects.filter(rama=rama)
        reuniones = Reunion.objects.filter(trimestre__in=trimestres)
        campamentos = Campamento.objects.filter(trimestre__in=trimestres)
        contenidos = Contenido.objects.filter(trimestre__in=trimestres)
        montes = Monte.objects.filter(rama=rama)
        talleres = Taller.objects.filter(rama=rama)
        simbolos = Simbolo.objects.filter(rama=rama)
        recursos = Recurso.objects.filter(rama=rama)
    except Rama.DoesNotExist:
        raise Http404("La rama no existe")

    context = {
        'rama_nombre': rama.get_nombre_display(),
        'rama_descripcion': rama.descripcion,
        'montes': montes,
        'trimestres': trimestres,
        'campamentos': campamentos,
        'reuniones': reuniones,
        'talleres': talleres,
        'simbolos': simbolos,
        'recursos': recursos,
        'contenidos': contenidos
        }

    return render(
        request, 
        'documentation/documentation.html',  
        context)
