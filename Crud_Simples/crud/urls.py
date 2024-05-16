from django.urls import path
from .views import index, listar_calcados, sobre_projeto, editar_calcados, remover_calcado
from .models import Calcado

urlpatterns = [
    path('', index, name='index'),
    path('listar-calcados',listar_calcados, name='listar-calcados'),
    path('sobre',sobre_projeto, name='sobre'),
    path('editar/<int:id>',editar_calcados, name='editar-calcados'),
    path('remover/<int:id>',remover_calcado, name='remover-calcados'),
]