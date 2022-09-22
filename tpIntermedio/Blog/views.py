from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from Blog.models import *
from django.http import HttpResponse
from Blog.forms import *
# Create your views here.

def inicio(request):
    return render(request, "Blog/inicio.html")

def crearEditor(request):
    if request.method == "POST":
        formEditor = formCreacionEditor(request.POST)
        if formEditor.is_valid():
            dataEditor = formEditor.cleaned_data
            nuevoEditor = Editor(username=dataEditor['username'], mail=dataEditor['mail'], edad=dataEditor['edad'])
            nuevoEditor.save()
            return render(request, "Blog/inicio.html")
    else:
        formEditor = formCreacionEditor()
    return render(request, "Blog/crearEditor.html", {"formEditor":formEditor})

def crearLector(request):
    if request.method == "POST":
        formLector = formCreacionLector(request.POST)
        if formLector.is_valid():
            dataLector = formLector.cleaned_data
            nuevoLector = Lector(username=dataLector['username'], mail=dataLector['mail'], edad=dataLector['edad'])
            nuevoLector.save()
            return render(request, "Blog/inicio.html")
    else:
        formLector = formCreacionLector()
    return render(request, "Blog/crearLector.html", {"formLector":formLector})

def pensarIdea(request):
    if request.method == "POST":
        formIdea = formCreacionIdea(request.POST)
        if formIdea.is_valid():
            dataIdea = formIdea.cleaned_data
            nuevaIdea = Ideas(tema=dataIdea['tema'], texto=dataIdea['texto'], autor=dataIdea['autor'], datetimePubl=datetime.now())
            nuevaIdea.save()
            return render(request, "Blog/inicio.html")
    else:
        formIdea = formCreacionIdea()
    return render(request, "Blog/pensarIdea.html", {"formIdea":formIdea})

def buscarenIdea(request):
    return render(request, 'Blog/buscarenIdea.html')

def resultadosIdea(request):
    if request.GET["termino"]:
        termino = request.GET["termino"]
        ideas = Ideas.objects.filter(texto__icontains=termino)

        return render(request, "Blog/resultadosIdea.html", {"termino":termino, "ideas":ideas})
    else:
        mensaje = "Enviar palabra clave para buscar ideas"
    return HttpResponse(mensaje)
    