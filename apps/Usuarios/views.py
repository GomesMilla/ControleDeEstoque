from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
import json



from Usuarios.SubViews import Cadastrar
from Usuarios.SubViews import Desativar
from Usuarios.SubViews import Editar
from Usuarios.SubViews import Listar

from Estoque.models import Produto
from Transacao.models import Movimentacao

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
            return redirect('ViewIndex')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            print("ALGUM DADO ERRADO! PRINCESA")
    
    context = {
        "nomePagina": "Controle de Estoque"
    }
    return render(request, 'Logins/Login.html', context)


def ViewIndex(request): 
    now = timezone.now()  
    mesAtual = now.month
    listUltimasCompras = []
    listUltimasVendas = []
    listProduto = Produto.objects.filter(ativo=True)
    nomes = [obj.nome for obj in listProduto]
    valorUnitarios = [int(obj.valorUnitario) for obj in listProduto]
    listMovimentacoes =  Movimentacao.objects.filter(dataCadastro__month=mesAtual).order_by("-dataCadastro")
    compras = [obj.tipoTransacao == "E" for obj in listMovimentacoes]
    saida = [obj.tipoTransacao == "S" for obj in listMovimentacoes]
    ultimasMovimentacoes = listMovimentacoes[:5]
    for movimentacao in listMovimentacoes:
        if movimentacao.tipoTransacao == "E":
            listUltimasCompras.append(movimentacao)
            listUltimasCompras[:5]
        else:
            listUltimasVendas.append(movimentacao)
            listUltimasVendas[:5]

    context = {
        "NomePagina" : "Início",
        "qtdProdutos" : len(listProduto),
        "qtdMovimentacaoMensal" : len(listMovimentacoes),
        "listUltimasCompras" : listUltimasCompras,
        "listUltimasVendas" : listUltimasVendas,
        'nomes': json.dumps(nomes),
        'valorUnitarios': json.dumps(valorUnitarios),
        'compras': json.dumps(compras),
        'vendas': json.dumps(saida),
        "listUltimasMovimentacoes":ultimasMovimentacoes,
        "listProduto":listProduto,
    }
    return render(request, "Usuarios/Index.html", context)



def Viewbase(request):
    context = {
        'now' : timezone.now().time(),
    }
    area_url = request.META.get('PATH_INFO')
    if request.user.is_authenticated and not "/admin/" in area_url:
        ObjUser = request.user
        context = {
            'now': timezone.now(),
            "ObjUser" : ObjUser,
        }
    
    return context





