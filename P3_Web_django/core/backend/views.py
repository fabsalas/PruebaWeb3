from django.shortcuts import render
#importamos las clases de los modelos
from .models import Producto

# Create your views here.

def base(request):
    #accediendo al objeto que contiene los datos de la base de datos
    #el metodo all traera todos los datos que estan en la tabla
    contexto = {}
    return render(request, 'base.html', contexto)

def signin(request):

    return render(request, 'signin.html',{})



def hardware(request):

    return render(request, 'hardware.html',{})


def mb(request):

    return render(request, 'mb.html',{})


def cpu(request):

    return render(request, 'cpu.html',{})


def gpu(request):

    return render(request, 'gpu.html',{})

def psu(request):

    return render(request, 'psu.html',{})

def ram(request):

    return render(request, 'ram.html',{})

def hdd(request):

    return render(request, 'hdd.html',{})

def sdd(request):

    return render(request, 'sdd.html',{})

def m2(request):

    return render(request, 'm2.html',{})