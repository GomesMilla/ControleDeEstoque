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
#     list_display = ['Pessoa', 'get_nomePessoa']
    # date_hierarchy = 'DataCadastro'
    # readonly_fields = ('DataCadastro','Nascimento','Cpf')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'Cnpj','estado') 
    list_filter = ('estado','cep')
    date_hierarchy = 'DataCadastro'
    readonly_fields = ('Cnpj','DataCadastro')
    search_fields = ['Nome']
    view_on_site = False



# Registrando a classe admin e acrescentando o novo modelo sobrescrevido
admin.site.register(Pessoa,PessoaAdmin) 
admin.site.register(Gerente)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vendedor)
