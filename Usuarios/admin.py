from django.contrib import admin
from Usuarios.models import *

# Sobrescrevendo a classe admin padrão!

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'Cpf','estado') #Dentro do admin na class Pessoas, é esses atributos que será mostrado
    list_filter = ('is_active','is_superuser','is_staff')#Filtrar Pessoas por esses atributos
    date_hierarchy = 'DataCadastro'
    readonly_fields = ('DataCadastro','Nascimento','Cpf')#Altera aqueles campos, deixando somente para leitura
    search_fields = ['Nome']#Campo de pesquisa por nome
    view_on_site = False


# class GerenteAdmin(admin.ModelAdmin):
#     list_display = ('Nome', 'Email', 'Cpf','estado')
#     list_filter = ('is_active','is_superuser','is_staff')
#     date_hierarchy = 'DataCadastro'
#     readonly_fields = ('DataCadastro','Nascimento','Cpf')

admin.site.register(Pessoa,PessoaAdmin)
# admin.site.register(Gerente)
# admin.site.register(Empresa)
# admin.site.register(Vendedor)
