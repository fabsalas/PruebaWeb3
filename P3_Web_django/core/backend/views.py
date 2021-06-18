from django.shortcuts import render

# Create your views here.

def base(request):

    return render(request, 'backend/Base.html')

def signin(request):

    return render(request, 'backend/Signin.html')

def signup(request):

    return render(request, 'backend/Signup.html')

def inicio(request):

    return render(request, 'backend/Inicio.html')