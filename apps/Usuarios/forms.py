from django import forms
from django.contrib.auth.models import User

from .models import  Pessoa, Empresa, Vendedor

class PessoaForm(forms.ModelForm):

    """
        Formulário para cadastrar as Pesssoas
    """

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user
    
    class Meta:
        model = Pessoa
        fields = ('__all__')

class EmpresaForm(forms.ModelForm):

    """
        Formulários para cadastro de Empresa
    """

    class Meta:
        model = Empresa
        exclude = ('dataCadastro',)


class VendedorForm(forms.ModelForm):

    """
        Formulário para cadastro de Vendedores
    """

    class Meta:
        model = Vendedor
        exclude = ('totalVendido', 'dataCadastro', 'dataDesativacao', 'desativadoPor', 'ativo')