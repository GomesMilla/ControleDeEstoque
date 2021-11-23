from django import forms
from .models import Sala


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        exclude = ('dataCadastro', 'ativo', 'desativadoPor', 'dataDesativacao')