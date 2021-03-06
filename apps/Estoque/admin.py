from django.contrib import admin
from .models import Estoque, Sala, Classificacao, Produto, LocalArmazenamentoProduto

# ModelAdminclasse é a representação de um modelo na interface administrativa
# Sintaxe para registrar todos os models de uma vez no admin
# @admin.register(Sala, Classificacao, Produto, LocalArmazenamentoProduto)
# class PersonAdmin(admin.ModelAdmin):
#     pass

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
    # readonly_fields = ('dataCadastro', 'cadastradoPor', 'desativadoPor', 'dataDesativacao')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'


class ProdutoPersonalizado(admin.ModelAdmin):
    list_display = ('nome', 'classificacao' ,'cadastradoPor', 'quantidadeMinima', 'valorUnitario', 'gerenteResposavel')
    list_filter = ['classificacao']
    radio_fields = {"classificacao": admin.VERTICAL}
    ordering = ['nome']
    search_fields = ['nome']
    # readonly_fields = ('dataCadastro', 'cadastradoPor', 'desativadoPor', 'dataDesativacao')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'


class LocalArmazenamentoProdutoPersonalizado(admin.ModelAdmin):
    list_display = ('sala', 'produto' ,'dataCadastro', 'cadastradoPor', 'ativo')
    list_filter = ['sala']
    ordering = ['sala']
    search_fields = ['sala']
    readonly_fields = ('dataCadastro', 'cadastradoPor', 'desativadoPor', 'dataDesativacao')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'

class EstoquePersonalizado(admin.ModelAdmin):
    list_display = ('produto' ,'valorEstoque', 'estoqueAtual', 'gerenteResposavel')
    list_filter = ['produto']
    ordering = ['produto']
    search_fields = ['produto']
    readonly_fields = ('dataCadastro', 'cadastradoPor')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'


admin.site.register(Sala, SalaPersonalizado)
admin.site.register(Classificacao, ClassificacaoPersonalizado)
admin.site.register(Produto, ProdutoPersonalizado)
admin.site.register(LocalArmazenamentoProduto, LocalArmazenamentoProdutoPersonalizado)
admin.site.register(Estoque, EstoquePersonalizado)