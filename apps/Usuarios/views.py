from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

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
    if request.user.is_authenticated: return redirect('ViewListarEmpresas')
    
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
        "NomePagina" : "Criar Conta",
        "FormularioVazio" : FormularioVazio
    }

    return render(request, "Cadastro/CadastroUser.html", context)

def ViewIndex(request):
    print(request.user.nome)
    
    context = {
        "NomePagina" : "Início",
    }
    return render(request, "Usuarios/Index.html", context)

def ViewCadastrarEmpresa(request):
    now = timezone.now()
    FormularioSimples = EmpresaForm(initial={ "cadastradoPor" : request.user,})    
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            objEmpresa = form.save(commit=False)
            objEmpresa.dataCadastro = now
            objEmpresa.cadastradoPor = request.user
            objEmpresa.ativo = True
            objEmpresa.save()
            mensagem = f'Empresa cadastrada com sucesso!'
            messages.success(request, mensagem) 
            return redirect("ViewListarEmpresas") 
        
        else:
            print(form.errors.as_data())  
    else:
        mensagem = f'Por favor! Preencha todos os campos corretamento para cadastrar a empresa!'
        messages.info(request, mensagem)
        FormularioSimples = EmpresaForm()             

    context = {
        "NomePagina" : "Criar Conta",
        "FormularioSimples" : FormularioSimples,
        "now" : now
    }

    return render(request, "Cadastro/CadastrarEmpresa.html", context)

def ViewListarEmpresas(request):

    ListEmpresas = Empresa.objects.filter(ativo=True)

    context = {
        "NomePagina" : "Empresas",
        "ListEmpresas" : ListEmpresas
    }
    return render(request, "Listar/ListaEmpresa.html", context)

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
    

def ViewEditarEmpresa(request, id_empresa):
    ObjEmpresa =  Empresa.objects.get(pk=id_empresa)

    if request.method == 'POST':
        FormularioPreenchido = EmpresaForm(request.POST or None, instance = ObjEmpresa)
        if FormularioPreenchido.is_valid():
            objEmpresa = FormularioPreenchido.save(commit=False)
            objEmpresa.ativo = True
            objEmpresa.save()
            mensagem = f'Alteração realizada com sucesso!'
            messages.success(request, mensagem) 
            return redirect("ViewListarEmpresas")
    else:
        FormularioPreenchido = EmpresaForm(instance=ObjEmpresa)
        print(FormularioPreenchido)

    context = {
        "NomePagina" : "Editar Empresa",
        "FormularioSimples" : FormularioPreenchido
    }

    return render(request, "Editar/EditarEmpresa.html", context)


# Construindo View
# def ViewVisualizarEmpresa(request, id_empresa):
#     ObjEmpresa = Empresa.objects.get(pk=id_empresa)

#     return render(request)




# Arrumar is_active da empresa. Ele já inicia sendo True


