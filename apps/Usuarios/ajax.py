from typing_extensions import TypeGuard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import PROTECT
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from Usuarios.models import Empresa, Pais



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

