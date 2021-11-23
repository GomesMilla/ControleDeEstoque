from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views  



from Usuarios.views import Cadastrar
from Usuarios.views import Listar
from Usuarios.views import Editar
from Usuarios.views import Desativar
from . import ajax


urlpatterns =[
    # INICIO DO SISTEMA
    path('Início/', ViewIndex, name="ViewIndex"),
    # USUÁRIOS
    path('Criar-Conta/', Cadastrar.ViewCriarConta, name="ViewCriarConta"),  
    
    
    # EMPRESA
    path('Cadastrar-Empresa', Cadastrar.ViewCadastrarEmpresa, name="ViewCadastrarEmpresa"),
    path('Lista-De-Empresas', Listar.ViewListarEmpresas, name="ViewListarEmpresas"),
    path('Desativar-Empresa/<int:id_empresa>/', Desativar.ViewDesativarEmpresa, name="ViewDesativarEmpresa"),
    path('Editar-Empresa/<int:id_empresa>/', Editar.ViewEditarEmpresa, name="ViewEditarEmpresa"),
    path('Movimentacoes-Empresa/<int:id_empresa>/', Listar.ViewListarMovimentacaoEmpresa, name="ViewListarMovimentacaoEmpresa"),

    # AJAX
    path('Ajax-Cadastrar-Empresa/', ajax.AjaxCadastroEmpresa, name="AjaxCadastroEmpresa"),


    # VENDEDOR
    path('Cadastrar-Vendedor', Cadastrar.ViewCadastrarVendedor, name="ViewCadastrarVendedor"),
    path('Desativar-Vendedor/<int:id_vendedor>/', Desativar.ViewDesativarVendedor, name="ViewDesativarVendedor"),
    path('Movimentacoes-Vendedor/<int:id_vendedor>/', Listar.ViewListarMovimentacaoVendedor, name="ViewListarMovimentacaoVendedor"),

    # REDEFINIÇÃO DE SENHAS
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Logins/forgot.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Logins/ResetDone.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Logins/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Logins/PasswordResetComplete.html"), name="password_reset_complete"),



]