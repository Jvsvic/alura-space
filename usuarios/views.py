from django.shortcuts import render
from usuarios.forms import Formulario

def login(request):
    form = Formulario()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
