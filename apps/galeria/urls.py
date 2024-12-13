from django.urls import path
from apps.galeria.views import index, imagem, buscar, new_imagem, editar_imagem, deletar_imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('new-imagem', new_imagem, name='new_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem', deletar_imagem, name='deletar_imagem'),
]