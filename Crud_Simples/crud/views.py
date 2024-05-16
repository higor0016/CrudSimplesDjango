from django.shortcuts import render, redirect, get_object_or_404    
from .form import FormCadProduto
from django.contrib import messages
from .models import Calcado
# Create your views here.
def index(request):
    if request.method == "POST":
        formulario = FormCadProduto(request.POST)
        if formulario.is_valid():
            formulario.save()
            #Fornecer mensagem de sucesso
            messages.success(request, 'Calçado cadastrado com sucesso!')
            return redirect(request.get_full_path())
        else:
            print("Formulário inválido")
    else:
        formulario = FormCadProduto()
    return render(request, 'static/pages/index.html', {'formulario':formulario})

#VIEW DE LISTAGEM DE CALÇADOS CADASTRADOS
def listar_calcados(request):
    calcados = Calcado.objects.all()
    return render(request, 'static/pages/calcados-listar.html', {'calcados':calcados})

#VIEW DE "SOBRE O PRJETO"
def sobre_projeto(request):
    return render(request, 'static/pages/sobre-projeto.html')

#VIEW DE "EDITAR CALÇADOS"
def editar_calcados(request, id):
    calcado = get_object_or_404(Calcado, id=id)
    if request.method == 'POST':
        form = FormCadProduto(request.POST, instance=calcado)
        if form.is_valid():
            form.save()
            return redirect('listar-calcados')  
    else:
        form = FormCadProduto(instance=calcado)
    return render(request, 'static/pages/calcados-editar.html', {'form':form})