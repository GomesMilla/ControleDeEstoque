from django.contrib import admin
from Usuarios.models import *

# Sobrescrevendo a classe admin padrão!
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf','estado','id') #Dentro do admin na class Pessoas, é esses atributos que será mostrado
    list_filter = ('is_active','is_superuser','is_staff')#Filtrar Pessoas por esses atributos
    date_hierarchy = 'dataCadastro'
    search_fields = ['nome']#Campo de pesquisa por nome
    view_on_site = False

class VendedorAdmin(admin.ModelAdmin):
    readonly_fields = ('totalVendido',)
    search_fields = ['nome']


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cnpj','estado', 'id') 
    list_filter = ('estado','cep')
    date_hierarchy = 'dataCadastro'
    search_fields = ['nome']
    view_on_site = False



# Registrando a classe admin e acrescentando o novo modelo sobrescrevido
admin.site.register(Pessoa,PessoaAdmin) 
admin.site.register(Gerente)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Pais)

####################################################################
# PESQUISAR readonly_fields
# class GerenteAdmin(ReadOnly.ModelAdmin):
#     list_display = ['id','Nome']
#     search_fields = ['Nome']
#     save_on_top = True
#     save_as = True
# Entender o modelo ReadOnly.ModelAdmin
