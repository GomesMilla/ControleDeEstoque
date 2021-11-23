from django.shortcuts import redirect, render
from .forms import SalaForm
from django.utils import timezone
from django.contrib import messages

def ViewCadastrarSala(request):
    now = timezone.now()
    objUser = request.user
    form = SalaForm(initial={'cadastradoPor': request.user,})

    if request.method == "POST":
        formulario = SalaForm(request.POST)
        if formulario.is_valid:
            objSala = formulario.save(commit=False) 
            objSala.dataCadastro = now
            objSala.ativo = True
            objSala.save()
            return redirect("ViewListarEmpresas")

        else:
            print(formulario.errors.as_data())
            messages.error(request, "Usuário ou senha inválidos!")
            print("ALGUM DADO ERRADO! PRINCESA")
    else:
        form = SalaForm(initial={'cadastradoPor': request.user,})

    context = {
        
        "NomePagina" : "Cadastrar Sala",
        "form" : form
    }

    return render(request, "Cadastro/CadastrarSala.html", context)
