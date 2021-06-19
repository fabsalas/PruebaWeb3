from django.shortcuts import render

# Create your views here.

def base(request):
    contexto = {}
    return render(request, 'base.html', contexto)

def signin(request):

    return render(request, 'signin.html',{})

def signup(request):

    return render(request, 'signup.html',{})

def hardware(request):

    return render(request, 'hardware.html')

