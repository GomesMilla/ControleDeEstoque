from django.contrib import admin
from .models import Sala, Classificacao, Produto, LocalArmazenamentoProduto

# ModelAdminclasse é a representação de um modelo na interface administrativa
# Sintaxe para registrar todos os models de uma vez no admin
# @admin.register(Sala, Classificacao, Produto, LocalArmazenamentoProduto)
# class PersonAdmin(admin.ModelAdmin):
#     pass


#  radio_fields = {"ativo": admin.VERTICAL}
class SalaPersonalizado(admin.ModelAdmin):
    list_display = ('nome', 'predio', 'andar', 'ativo')
    list_filter = ['ativo']
    ordering = ['nome']
    search_fields = ['nome']
    readonly_fields = ('dataCadastro', 'cadastradoPor', 'desativadoPor', 'dataDesativacao')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'

class ClassificacaoPersonalizado(admin.ModelAdmin):
    list_display = ('nome', 'cadastradoPor', 'dataCadastro')
    list_filter = ['ativo']
    ordering = ['nome']
    search_fields = ['nome']
    readonly_fields = ('dataCadastro', 'cadastradoPor', 'desativadoPor', 'dataDesativacao')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'


admin.site.register(Sala, SalaPersonalizado)
admin.site.register(Classificacao, ClassificacaoPersonalizado)