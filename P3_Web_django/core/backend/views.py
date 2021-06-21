from django.shortcuts import redirect, render
#importamos las clases de los modelos
from .models import  Componente, Fabricante, Producto

# Create your views here.

def base(request):
    #accediendo al objeto que contiene los datos de la base de datos
    #el metodo all traera todos los datos que estan en la tabla
    
    contexto = {}
    return render(request, 'base.html', contexto)

def signin(request):

    return render(request, 'signin.html',{})



def productos(request):
    productos= Producto.objects.all()
    contexto = {'productos' : productos}
    return render(request, 'productos.html',contexto)


def AgregarProducto(request):
    agr_producto = Producto.objects.all()

    contexto = {'agr_producto': agr_producto}
    return render(request, 'productos.html', contexto)


def Form_Productos(request):
    fabricantes = Fabricante.objects.all()

    contexto={'fabricantes': fabricantes}
    return render(request, 'agregar_prod.html', contexto)

def Form_Productos_1(request):
    componentes = Componente.objects.all()

    contexto={'componentes': componentes}
    return render(request, 'agregar_prod.html', contexto)


def Guardar_Prod(request):
    nombre      = request.POST.get('nombre','')
    fabricantes = request.POST.get('fabricantes','')
    componentes = request.POST.get('componentes','')
    precio      = request.POST.get('precio','')
    stock       = request.POST.get('stock','')
    imagen      = request.FILES.get('imagen','')

    productos_g= Producto(nombre=nombre, fabricantes =fabricantes, componentes= componentes, precio= precio, stock= stock, imagen= imagen)
    productos_g.save()
    
    return redirect(to='productos')
    




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
