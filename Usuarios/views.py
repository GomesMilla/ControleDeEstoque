from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone


def ViewCriarConta(request):
    FormularioVazio = PessoaForm()
    if request.method == 'POST':
        print("Dentro metodo post")
        FormularioPreenchido = PessoaForm(request.POST)
        print(FormularioPreenchido)
        if FormularioPreenchido.is_valid():
            print("formulario valido")
            FormularioPreenchido.save()
            
            return redirect("Login") 
        
        else:
            print(FormularioPreenchido.errors.as_data())               


    context = {
        "nome_pagina" : "Criar Conta",
        "FormularioVazio" : FormularioVazio
    }

    return render(request, "Logins/CadastroUser.html", context)

def ViewIndex(request):

    context = {
        "nome_pagina" : "Início",
    }
    return render(request, "Usuarios/Index.html", context)

def ViewCadastrarEmpresa(request):

    FormularioSimples = EmpresaForm()
    now = timezone.now()    
    
    if request.method == 'POST':
        print("Dentro metodo post")
        FormularioPreenchido = EmpresaForm(request.POST)
        print(FormularioPreenchido)
        if FormularioPreenchido.is_valid():
            print("formulario valido")
            FormularioPreenchido.save()
            mensagem = f'Empresa cadastrada com sucesso!'
            messages.success(request, mensagem) 
            return redirect("ViewIndex") 
        
        else:
            print(FormularioPreenchido.errors.as_data())               

    context = {
        "nome_pagina" : "Criar Conta",
        "FormularioSimples" : FormularioSimples,
        "now" : now
    }

    return render(request, "Usuarios/CadastrarEmpresa.html", context)

def ViewListarEmpresas(request):

    ListEmpresas = Empresa.objects.filter(is_active = True)

    context = {
        "nome_pagina" : "Empresas",
        "ListEmpresas" : ListEmpresas
    }
    return render(request, "Usuarios/ListaEmpresa.html", context)

def ViewDesativarEmpresa(request, id_empresa):

    ObjEmpresa = Empresa.objects.get(pk = id_empresa)
    ObjEmpresa.is_active = False
    ObjEmpresa.save()
    mensagem = f'Empresa removida com sucesso!'
    messages.warning(request, mensagem) 
    return redirect("ViewListarEmpresas")
    

    context = {
        "nome_pagina" : "Desativar Empresa",
    }

    return render(request, 'Usuarios/Index.html', context)






