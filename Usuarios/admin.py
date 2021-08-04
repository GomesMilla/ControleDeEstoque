from django.contrib import admin
from Usuarios.models import *

# Sobrescrevendo a classe admin padrão!
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'email', 'Cpf','estado','id') #Dentro do admin na class Pessoas, é esses atributos que será mostrado
    list_filter = ('is_active','is_superuser','is_staff')#Filtrar Pessoas por esses atributos
    date_hierarchy = 'DataCadastro'
    search_fields = ['Nome']#Campo de pesquisa por nome
    view_on_site = False

class VendedorAdmin(admin.ModelAdmin):
    readonly_fields = ('TotalComprado',)
    search_fields = ['Nome']


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'email', 'Cnpj','estado', 'id') 
    list_filter = ('estado','cep')
    date_hierarchy = 'DataCadastro'
    search_fields = ['Nome']
    view_on_site = False



# Registrando a classe admin e acrescentando o novo modelo sobrescrevido
admin.site.register(Pessoa,PessoaAdmin) 
admin.site.register(Gerente)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vendedor, VendedorAdmin)

####################################################################
# PESQUISAR readonly_fields
# class GerenteAdmin(ReadOnly.ModelAdmin):
#     list_display = ['id','Nome']
#     search_fields = ['Nome']
#     save_on_top = True
#     save_as = True
# Entender o modelo ReadOnly.ModelAdmin
