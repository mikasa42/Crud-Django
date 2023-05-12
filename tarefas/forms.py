from django import forms

from .models import tarefa

class tarefaForm(forms.ModelForm):
    class Meta:
        model = tarefa
        fields = ('title', 'description')