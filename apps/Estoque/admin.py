from django.contrib import admin
from .models import Sala, Classificacao, Produto, LocalArmazenamentoProduto

# ModelAdminclasse é a representação de um modelo na interface administrativa
# Sintaxe para registrar todos os models de uma vez no admin
# @admin.register(Sala, Classificacao, Produto, LocalArmazenamentoProduto)
# class PersonAdmin(admin.ModelAdmin):
#     pass

class SalaPersonalizado(admin.ModelAdmin):
    list_display = ('nome', 'predio', 'andar', 'ativo')
    fields = ('nome','descricao','ativo'('predio', 'andar'))
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'

admin.site.register(Sala, SalaPersonalizado)