from django.urls import path
from .views import index, listar_calcados, sobre_projeto, editar_calcados
from .models import Calcado

urlpatterns = [
    path('', index, name='index'),
    path('listar-calcados',listar_calcados, name='listar-calcados'),
    path('sobre',sobre_projeto, name='sobre'),
    path('editar/<int:id>',editar_calcados, name='editar-calcados'),
]