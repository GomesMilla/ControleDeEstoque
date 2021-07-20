from django import forms
from .models import *
from django.contrib.auth.models import User

class PessoaForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user
    
    class Meta:
        model = Pessoa
        fields = ["Nome","Naturalidade","Pais","Escolaridade", "Status", "Email", "Telefone_celular", "Cpf", "Nascimento","EstadoCivil","Profissao", "cep","estado","cidade","bairro","logradouro","Numero","DataCadastro","password"]