from django.shortcuts import redirect, render
from .forms import SalaForm
from django.utils import timezone
from django.contrib import messages

def ViewCadastrarSala(request):
    now = timezone.now()
    form = SalaForm()

    if request.method == "POST":
        formulario = SalaForm(request.POST)
        if formulario.is_valid:
            objSala = formulario.save(commit=False) 
            objSala.dataCadastro = now
            objSala.cadastradoPor = request.user
            objSala.ativo = True
            objSala.save()
            redirect("ViewListarEmpresas")
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            print("ALGUM DADO ERRADO! PRINCESA")
    else:
        form = SalaForm()

    context = {
        
        "NomePagina" : "Cadastrar Sala",
        "form" : form
    }

    return render(request, "Cadastro/CadastrarSala.html", context)
