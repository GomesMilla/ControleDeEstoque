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
    print(request.user.nome)
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
            FormularioPreenchido.is_active = True
            FormularioPreenchido.save()
            mensagem = f'Empresa cadastrada com sucesso!'
            messages.success(request, mensagem) 
            return redirect("ViewListarEmpresas") 
        
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
    ObjEmpresa = Empresa.objects.get(id = id_empresa)
    ObjEmpresa.is_active = False
    ObjEmpresa.save()
    mensagem = f'Empresa desativada com sucesso!'
    messages.warning(request, mensagem) 
    return redirect("ViewListarEmpresas")
    
    context = {
        "nome_pagina" : "Desativar Empresa",
    }

    return render(request, 'Usuarios/Index.html', context)

def ViewEditarEmpresa(request, id_empresa):
    print(id_empresa)
    ObjEmpresa =  Empresa.objects.get(pk=id_empresa)
    print(request.method)

    if request.method == 'POST':
        FormularioPreenchido = EmpresaForm(request.POST or None, instance = ObjEmpresa)
        if FormularioPreenchido.is_valid():
            ObjEmpresa.is_active = True
            FormularioPreenchido.save()
            mensagem = f'Alteração realizada com sucesso!'
            messages.success(request, mensagem) 
            return redirect("ViewListarEmpresas")
    else:
        FormularioPreenchido = EmpresaForm(instance=ObjEmpresa)
        print(FormularioPreenchido)

    context = {
        "nome_pagina" : "Editar Empresa",
        "FormularioSimples" : FormularioPreenchido
    }

    return render(request, "Usuarios/EditarEmpresa.html", context)


# Construindo View
# def ViewVisualizarEmpresa(request, id_empresa):
#     ObjEmpresa = Empresa.objects.get(pk=id_empresa)

#     return render(request)




# Arrumar is_active da empresa. Ele já inicia sendo True


