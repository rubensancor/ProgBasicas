import os
import re
import markdown
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from markdown import markdown

from progbasicas.settings import STATICFILES_DIRS

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
        ramas = Rama.objects.all()
        rama = Rama.objects.get(nombre__iexact=rama_name)
        trimestres = Trimestre.objects.filter(rama=rama)
        reuniones = Reunion.objects.filter(trimestre__in=trimestres)
        campamentos = Campamento.objects.filter(trimestre__in=trimestres)
        contenidos_rama = ContenidoRama.objects.filter(rama=rama)
        contenidos_trimestre = ContenidoTrimestre.objects.filter(
            trimestre__in=trimestres)
        montes = Monte.objects.filter(rama=rama)
        talleres = Taller.objects.filter(rama=rama)
        simbolos = Simbolo.objects.filter(rama=rama)
        recursos = Recurso.objects.filter(trimestre__in=trimestres)
        markdowntext = get_markdown_data(rama_name)
    except Rama.DoesNotExist:
        raise Http404("La rama no existe")

    context = {
        'ramas': ramas,
        'rama_nombre': rama.get_nombre_display(),
        'rama_descripcion': rama.descripcion,
        'montes': montes,
        'trimestres': trimestres,
        'campamentos': campamentos,
        'reuniones': reuniones,
        'talleres': talleres,
        'simbolos': simbolos,
        'recursos': recursos,
        'contenidos_rama': contenidos_rama,
        'contenidos_trimestre': contenidos_trimestre,
        }
    context.update(markdowntext)
    return render(
        request, 
        'documentation/'+str(rama)+'.html',  
        context)

def get_markdown_data(rama_name):
    sections = []
    context = {}
    path = os.path.join(STATICFILES_DIRS[0], 'md/'+rama_name)
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            for line in f.readlines():
                if '[comment]' in line:
                    sections.append(re.search('\((.*)\)', line).group(1))
                    break
        with open(os.path.join(path, filename), 'r') as f:
            context[str(filename.split('-')[1].split('.md')[0])] = f.read()
            context['sections'] = sections
    return context
    
