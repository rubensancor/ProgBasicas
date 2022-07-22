from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('documentation/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def er_documentation(request, er_name):
    template = loader.get_template('documentation/documentation.html')
    context = {}
    return HttpResponse(template.render(context, request))
