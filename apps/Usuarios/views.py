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
            return redirect('ViewListarEmpresas')
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
    listProduto = Produto.objects.filter(ativo=True)
    nomes = [obj.nome for obj in listProduto]
    valorUnitarios = [int(obj.valorUnitario) for obj in listProduto]
    # categorias = [int(obj.categoria) for obj in listProduto]

    listCompra = []
    listVenda = []
    listUltimasCompras = []
    listUltimasVendas = []
    listProdutos = Produto.objects.all()
    listServicos =  Movimentacao.objects.filter(dataCadastro__month=mesAtual).order_by("-dataCadastro")  
    ultimasMovimentacoes =  listServicos[:5]

    for servico in listServicos:
        if servico.tipoTransacao == "E" :
            listCompra.append(servico)
            listUltimasCompras = listCompra[:5]
        else:
            listVenda.append(servico)
            listUltimasVendas = listVenda[:5]
    

    context = {
        "NomePagina" : "Início",
        "qtdProdutos" : len(listProdutos),
        "qtdMovimentacaoMensal" : len(listServicos),
        "qtdCompra" : len(listCompra),
        "qtdVendas": len(listVenda),
        "listUltimasMovimentacoes" : ultimasMovimentacoes,
        "listUltimasCompras" : listUltimasCompras,
        "listUltimasVendas" : listUltimasVendas,
        'nomes': json.dumps(nomes),
        'valorUnitarios': json.dumps(valorUnitarios),
        # 'categorias': json.dumps(categorias),
        "listProduto":listProduto,
    }
    return render(request, "Usuarios/Index.html", context)



