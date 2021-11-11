from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from Usuarios.models import Empresa, Vendedor
from Transacao.models import Movimentacao


def ViewListarEmpresas(request):

    ListEmpresas = Empresa.objects.filter(ativo=True)

    context = {
        "NomePagina" : "Empresas",
        "ListEmpresas" : ListEmpresas
    }
    return render(request, "Listar/ListaEmpresa.html", context)


def ViewListarMovimentacaoEmpresa(request, id_empresa):
    objEmpresa = Empresa.objects.get(pk=id_empresa)
    nome = objEmpresa.nome
    listMovimentacao = Movimentacao.objects.filter(empresaTransacao=objEmpresa).order_by("dataCadastro")
    listVendedores = Vendedor.objects.filter(empresa=objEmpresa).order_by("-ativo")

    context = {
        "NomePagina" : nome,
        "objEmpresa" : objEmpresa,
        "listMovimentacao" : listMovimentacao,
        "listVendedores": listVendedores,
    }

    return render (request, "Listar/ListarMovimentacoes.html", context)