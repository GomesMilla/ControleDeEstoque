from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views  #Importando pacote Django padrão para recuperação de senha 


urlpatterns =[
    path('Criar-Conta/', ViewCriarConta, name="ViewCriarConta"),
    path('Início/', ViewIndex, name="ViewIndex"),
    path('Cadastrar-Empresa', ViewCadastrarEmpresa, name="ViewCadastrarEmpresa"),
    path('Lista-De-Empresas', ViewListarEmpresas, name="ViewListarEmpresas"),
    path('Desativar-Empresa/<int:id_empresa>/', ViewDesativarEmpresa, name="ViewDesativarEmpresa"),
    path('Editar-Empresa/<int:id_empresa>/', ViewEditarEmpresa, name="ViewEditarEmpresa"),

    # REDEFINIÇÃO DE SENHAS
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Logins/forgot.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Logins/ResetDone.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Logins/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Logins/PasswordResetComplete.html"), name="password_reset_complete"),



]