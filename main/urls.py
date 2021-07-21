from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView #Importando a View Login padrão do Django 
from django.contrib.auth import views as auth_views  #Importando pacote Django padrão para recuperação de senha 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuarios.urls')), #Incluindo a rota da Url criada no aplicativo url
    path('', LoginView.as_view(template_name='Logins/Login.html'), name='Login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Logins/forgot.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Logins/ResetDone.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Logins/reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="Logins/PasswordResetComplete.html"), name="password_reset_complete"),


]
