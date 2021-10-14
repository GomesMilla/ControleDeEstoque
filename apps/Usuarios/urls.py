from django.urls import path
from .views import *


urlpatterns =[
    path('Criar-Conta/', ViewCriarConta, name="ViewCriarConta"),
    path('Início/', ViewIndex, name="ViewIndex"),
    path('Cadastrar-Empresa', ViewCadastrarEmpresa, name="ViewCadastrarEmpresa"),
    path('Lista-De-Empresas', ViewListarEmpresas, name="ViewListarEmpresas"),
    path('Desativar-Empresa/<int:id_empresa>/', ViewDesativarEmpresa, name="ViewDesativarEmpresa"),
    path('Editar-Empresa/<int:id_empresa>/', ViewEditarEmpresa, name="ViewEditarEmpresa"),



]