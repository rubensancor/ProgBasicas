import os
import re
import markdown
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from markdown import markdown

from progbasicas.settings.base import BASE_DIR

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
        salidas = Salida.objects.filter(rama=rama)
        talleres = Taller.objects.filter(rama=rama)
        markdowntext = get_markdown_data(rama_name)
    except Rama.DoesNotExist:
        raise Http404("La rama no existe")

    context = {
        'ramas': ramas,
        'rama_nombre': rama.get_nombre_display(),
        'rama_descripcion': rama.descripcion,
        'salidas': salidas,
        'talleres': talleres,
        }
    context.update(markdowntext)
    print(context)
    return render(
        request, 
        'documentation/documentation.html',
        context)

def get_markdown_data(rama_name):
    context = {}
    num = 1
    sidebar_sections = {}
    sections_text = {}

    path = os.path.join(BASE_DIR, 'static/md/'+rama_name)
    
    for filename in sorted(os.listdir(path)):
        sections_text[num] = {}
        sidebar_sections[num] = {}

        # Handle comments
        with open(os.path.join(path, filename), 'r') as f:
            for line in f.readlines():
                if '[nombre]' in line:
                    sections_text[num]['name'] = (re.search('\((.*)\)', line).group(1))
                elif '[sidebar]' in line:
                    sidebar_sections[num]['sidebar'] = (re.search('\((.*)\)', line).group(1))
                elif '[icon]' in line:
                    sidebar_sections[num]['icon'] = (re.search('\((.*)\)', line).group(1))
                elif '[exit]' in line:
                    break
                    
        # Dictionary for the contents
        with open(os.path.join(path, filename), 'r') as f:
            sections_text[num]['filename'] = str(filename.split('-')[1].split('.md')[0])
            sections_text[num]['text'] = f.read()
        num += 1   

        context['sections_text'] = sections_text
        context['sidebar_sections'] = sidebar_sections
    return context
    
