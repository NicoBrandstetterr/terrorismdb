from django.http import HttpResponse
from django.shortcuts import render
from terrorismapp.models import Gname

def seleccion_preguntas(request):
    return render(request,"principal.html")


def primeraQuery(request):
    #query=gName.objects.raw('SELECT * FROM terrorismapp_gname WHERE gname = Hutu extremists')
    query=Gname.objects.filter(gname='Hutu extremists')
    return render(request, "1query.html",{"Tabla":query})


def segundaQuery(request):
    #query=gName.objects.raw('SELECT * FROM Tabla2 WHERE gname = "Hutu extremists"')
    query=Gname.objects.filter(gname='Hutu extremists')
    return render(request, "2query.html",{"Tabla2":query})

def terceraQuery(request):
    #query=gName.objects.raw('SELECT * FROM Tabla3 WHERE gname = "Hutu extremists"')
    query=Gname.objects.filter(gname='Hutu extremists')
    return render(request, "3query.html",{"Tabla3":query})