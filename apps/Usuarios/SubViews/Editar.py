from Usuarios.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout



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