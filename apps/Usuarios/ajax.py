from typing_extensions import TypeGuard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import PROTECT
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from Usuarios.models import Empresa, Pais, Pessoa
from django.http import JsonResponse



@login_required
def AjaxCadastroEmpresa(request):
    now = timezone.now()
    nomeEmpresa = request.GET.get('nomeEmpresa', None)
    EmailEmpresa = request.GET.get('EmailEmpresa', None)
    ContatoEmpresa = request.GET.get('ContatoEmpresa', None)
    CNPJEmpresa = request.GET.get('CNPJEmpresa', None)
    PaisEmpresa = request.GET.get('PaisEmpresa', None)
    Cep = request.GET.get('Cep', None)
    Estado = request.GET.get('Estado', None)
    Cidade = request.GET.get('Cidade', None)
    Logradouro = request.GET.get('Logradouro', None)
    Bairro = request.GET.get('Bairro', None)
    objPais =  Pais.objects.get(pk=PaisEmpresa)
    
    objEmpresa = Empresa()
    objEmpresa.nome = nomeEmpresa
    objEmpresa.email =EmailEmpresa
    objEmpresa.cnpj = CNPJEmpresa
    objEmpresa.telefone = ContatoEmpresa
    objEmpresa.pais = objPais
    objEmpresa.cep =  Cep
    objEmpresa.estado = Estado
    objEmpresa.cidade = Cidade
    objEmpresa.bairro = Bairro
    objEmpresa.logradouro = Logradouro
    objEmpresa.cadastradoPor = request.user
    objEmpresa.dataCadastro = now
    objEmpresa.ativo = True
    objEmpresa.save()

    listEmpresas = Empresa.objects.filter(ativo=True)

    data = serializers.serialize('json', listEmpresas)
    return HttpResponse(data, content_type="application/json")


def AjaxCadastrarUsuario(request):
    now = timezone.now()
    nomePessoa = request.GET.get('nomeUsuario', None)
    EmailPessoa = request.GET.get('EmailUsuario', None)
    cpf = request.GET.get('CPFUsuario', None)
    ContatoPessoa = request.GET.get('ContatoUsuario', None)
    DataNascimento = request.GET.get('NascimentoUsuario', None)
    PaisPessoa = request.GET.get('PaisUsuario', None)
    Cep = request.GET.get('Cep', None)
    Estado = request.GET.get('Estado', None)
    Cidade = request.GET.get('Cidade', None)
    Logradouro = request.GET.get('Logradouro', None)
    Bairro = request.GET.get('Bairro', None)
    objPais =  Pais.objects.get(pk=PaisPessoa)
    
    objPessoa = Pessoa()
    objPessoa.nome = nomePessoa
    objPessoa.email = EmailPessoa
    objPessoa.cpf = cpf
    objPessoa.dataDascimento = DataNascimento
    objPessoa.telefone = ContatoPessoa
    objPessoa.pais = objPais
    objPessoa.cep =  Cep
    objPessoa.estado = Estado
    objPessoa.cidade = Cidade
    objPessoa.bairro = Bairro
    objPessoa.logradouro = Logradouro
    objPessoa.cadastradoPor = request.user
    objPessoa.dataCadastro = now
    objPessoa.ativo = True
    objPessoa.save()

    listPessoas = Pessoa.objects.filter(ativo=True)

    data = serializers.serialize('json', listPessoas)
    return HttpResponse(data, content_type="application/json")


def AjaxVerificarEmail(request):
    email = request.GET.get('Email', None)
        
    data = {
        'is_taken': Pessoa.objects.filter(email__iexact=email).exists()
    }
    if not data['is_taken']:
        data['error_message'] = 'E-mail não cadastrado!'

    return JsonResponse(data)


