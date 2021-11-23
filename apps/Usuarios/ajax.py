from typing_extensions import TypeGuard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.deletion import PROTECT
from .models import Clinica, Equipe, FilaPaciente, Intervalo, SalaAtendimento, SemestreLetivo, Vendedor
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail



# @login_required
# def AjaxVerificarCadastroVendedor(request):
#     nome = request.GET.get('nomeIntervalo', None)
#     empresa = request.GET.get('tipoIntervalo', None)
    
#     try:
#         objVendedor = Vendedor.objects.get(pessoa)
#     except:
#         pass

#     listIntervalos = Intervalo.objects.filter(clinica__id=id_clinica,ativo=True)

#     data = serializers.serialize('json', listIntervalos)
#     return HttpResponse(data, content_type="application/json")

