from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import tarefaForm
from .models import tarefa

# Create your views here.

def tarefas(request):
    Tarefas = tarefa.objects.all().order_by('-creat_at')
    return render(request,'tarefas/lista.html',{'Tarefas':Tarefas})

def tarefaView(request, id):
    Tarefas = get_object_or_404(tarefa, pk=id)
    return render(request, 'tarefas/tarefa.html',{'Tarefas':Tarefas})

def adicionarTarefa(request):
    if request.method=="POST":
        form = tarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.done = 'doing'
            tarefa.save()
            return redirect('/')

    else:
        form = tarefaForm()
        return render(request, 'tarefas/adicionarTarefa.html', {'form':form})
def editarTarefa(request, id):
    Tarefa = get_object_or_404(tarefa, pk=id) # Ele tenta achar a view, senão da erro 404 para o usuario
    form = tarefaForm(instance=Tarefa)

    if(request.method == 'POST'):
        form = tarefaForm(request.POST, instance=Tarefa)
        if(form.is_valid()):
            Tarefa.save()
            return redirect('/')
        else:
            return render(request,'tarefas/editarTarefa.html', {'form':form, 'Tarefa':Tarefa})
        
    else:
        return render(request,'tarefas/editarTarefa.html', {'form':form, 'Tarefa':Tarefa})
def deletarTarefa(request, id):
    Tarefa = get_object_or_404(tarefa, pk=id) # Só vai deletar o registro encontrado
    Tarefa.delete()
    return redirect('/')

def index(request):
    return HttpResponse('Ola mundo')


def seunome(request, name):
    return render(request, 'tarefas/seunome.html', {'name': name})
