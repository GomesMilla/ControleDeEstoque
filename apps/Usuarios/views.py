from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout



from Usuarios.SubViews import Cadastrar
from Usuarios.SubViews import Desativar
from Usuarios.SubViews import Editar
from Usuarios.SubViews import Listar




def ViewInicio(request):

    context = {
        "NomePagina": "Controle de Estoque"
    }

    return render(request, "Apresentacao/Inicio.html", context)

def ViewObjetivos(request):

    context = {
        "NomePagina": "Objetivos"
    }

    return render(request, "Apresentacao/Objetivos.html", context)


def ViewPublicoAlvo(request):

    context = {
        "NomePagina": "Público Alvo"
    }

    return render(request, "Apresentacao/PublicoAlvo.html", context)

def ViewLogin(request):
    if request.user.is_authenticated: return redirect('ViewIndex')
    
    if request.method == "POST":
        user = authenticate(email = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('ViewListarEmpresas')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            print("ALGUM DADO ERRADO! PRINCESA")
    
    context = {
        "nomePagina": "Controle de Estoque"
    }
    return render(request, 'Logins/Login.html', context)


def ViewIndex(request):
    print(request.user.nome)
    
    context = {
        "NomePagina" : "Início",
    }
    return render(request, "Usuarios/Index.html", context)



