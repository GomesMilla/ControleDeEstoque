from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Movimentacao

class MovimentacaoPersonalizado(admin.ModelAdmin):
    list_display = ('tipoTransacao', 'empresaVendendora', 'vendendor','dataCadastro', 'produto', 'resposavel')
    list_filter = ['tipoTransacao']
    ordering = ['tipoTransacao']
    search_fields = ['sala']
    readonly_fields = ('dataCadastro', 'resposavel')
    empty_value_display = 'Não Informado'
    date_hierarchy = 'dataCadastro'

admin.site.register(Movimentacao, MovimentacaoPersonalizado)
