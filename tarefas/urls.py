from django.urls import path

from . import views
urlpatterns = [
    path('index/', views.index),
    path('', views.tarefas, name="lista-tarefas"),
    path('tarefas/<int:id>', views.tarefaView, name="tarefa-view"),
    path('adicionarTarefa/', views.adicionarTarefa, name="adicionar-tarefa"),
    path('editar/<int:id>', views.editarTarefa, name="editar-tarefa"),
    path('deletar/<int:id>', views.deletarTarefa, name="deletar-tarefa"),
    path('seunome/<str:name>', views.seunome, name="seu-nome"),
]