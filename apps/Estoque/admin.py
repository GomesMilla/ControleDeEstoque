from django.contrib import admin
from .models import *

# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ('Nome', 'Categoria','id') 
#     list_filter = ['Categoria']
#     search_fields = ['Nome']
#     view_on_site = False

admin.site.register(Produto)
# admin.site.register(Armazenamento)
