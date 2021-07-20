from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login


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

