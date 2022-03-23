from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout


from Usuarios.models import Empresa, Vendedor


def ViewDesativarEmpresa(request, id_empresa):
    now = timezone.now()
    ObjEmpresa = Empresa.objects.get(id = id_empresa)
    ObjEmpresa.ativo = False
    ObjEmpresa.dataDesativacao = now
    ObjEmpresa.desativadoPor = request.user
    ObjEmpresa.save()
    mensagem = f'Empresa desativada com sucesso!'
    messages.warning(request, mensagem) 
    return redirect("ViewListarEmpresas")


def ViewDesativarVendedor(request, id_vendedor):
    now = timezone.now()
    objVendedor = Vendedor.objects.get(pk=id_vendedor)
    objEmpresa = objVendedor.empresa        
    if objVendedor.ativo:       
        objVendedor.ativo = False
        objVendedor.dataDesativacao = now
        objVendedor.desativadoPor =  request.user
        objVendedor.save()
        mensagem = f'Vendedor desativada com sucesso!'
        messages.warning(request, mensagem)
    else:
        objVendedor.ativo = True
        objVendedor.dataDesativacao = now
        objVendedor.desativadoPor =  request.user
        objVendedor.save()
        mensagem = f'Vendedor desativada com sucesso!'
        messages.warning(request, mensagem)
    return redirect('ViewListarMovimentacaoEmpresa', objEmpresa.id)
