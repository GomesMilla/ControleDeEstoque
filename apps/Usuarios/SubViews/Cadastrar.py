from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from Usuarios.forms import PessoaForm, EmpresaForm, VendedorForm


def ViewCriarConta(request):
    FormularioVazio = PessoaForm()
    if request.method == 'POST':
        FormularioPreenchido = PessoaForm(request.POST)
        print(FormularioPreenchido)
        if FormularioPreenchido.is_valid():
            FormularioPreenchido.save()            
            return redirect("ViewListarEmpresas") 
        
        else:
            print(FormularioPreenchido.errors.as_data())               


    context = {
        "NomePagina" : "Criar Conta",
        "FormularioVazio" : FormularioVazio
    }

    return render(request, "Cadastro/CadastroUser.html", context)


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

def ViewCadastrarVendedor(request):
    now = timezone.now()
    objUser = request.user
    form = VendedorForm(initial={'cadastradoPor': objUser})

    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("ViewListarEmpresas")
        else:
            print(form.errors.as_data()) 
    else:
        form = VendedorForm(initial={'cadastradoPor': objUser, 'dataCadastro':now})


    context = {
        "NomePagina" : "Cadastrar Vendedor",
        "form" : form,
    }

    return render(request, "Cadastro/CadastrarVendedor.html", context)
            



