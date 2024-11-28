from django import forms

from .models import tarefa

class tarefaForm(forms.ModelForm):
    class Meta:
        model = tarefa
        fields = ('title', 'description')

    title = forms.CharField(label='Título da Tarefa')  # Nome personalizado
    description = forms.CharField(label='Descrição Detalhada')  # Nome personalizado