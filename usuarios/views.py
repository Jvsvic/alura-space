from django.shortcuts import render, redirect
from usuarios.forms import Formulario, CadastroForms

def login(request):
    form = Formulario()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form['senha_1'].value() != form['senha_2'].value():
            return redirect('cadastro')
    return render(request, 'usuarios/cadastro.html', {"form": form})

