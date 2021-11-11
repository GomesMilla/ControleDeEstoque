from django import forms
from .models import Sala


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        exclude = ('dataCadastro', 'cadastradoPor', 'ativo', 'desativadoPor', 'dataDesativacao')