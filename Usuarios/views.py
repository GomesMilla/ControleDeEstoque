from .forms import *
from django.shortcuts import render, redirect
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
            
            return redirect("ViewIndex") 
        
        else:
            print(FormularioPreenchido.errors.as_data())               

    mensagem = f'Empresa cadastrada com sucesso!'
    messages.success(request, mensagem)  
    context = {
        "nome_pagina" : "Criar Conta",
        "FormularioSimples" : FormularioSimples,
        "now" : now
    }

    return render(request, "Usuarios/CadastrarEmpresa.html", context)



