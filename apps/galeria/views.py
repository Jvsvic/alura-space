from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

def index(request):
        if not request.user.is_authenticated:
                messages.error(request, 'Você precisa estar logado')
                return redirect('login')
        fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
        return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
        fotografia = get_object_or_404(Fotografia, pk=foto_id)
        return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar'].strip()
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})  # Corrigido: fechando o parêntese


def new_imagem(request):
        return render(request, 'galeria/new_imagem.html')

def editar_imagem(request):
      pass

def deletar_imagem(request):
    pass        