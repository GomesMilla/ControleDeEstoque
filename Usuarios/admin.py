from django.contrib import admin
from Usuarios.models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'Cpf','estado')
    list_filter = ('is_active','is_superuser','is_staff')
    date_hierarchy = 'DataCadastro'
    readonly_fields = ('DataCadastro','Nascimento','Cpf')

admin.site.register(Pessoa,PessoaAdmin)
# admin.site.register(Gerente)
# admin.site.register(Empresa)
# admin.site.register(Vendedor)
