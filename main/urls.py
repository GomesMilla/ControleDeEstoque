from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView #Importando a View Login padrão do Django 
from Usuarios import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuarios.urls')), #Incluindo a rota da Url criada no aplicativo url
    
    # URLS DE INICIO
    path('', views.ViewInicio, name="ViewInicio"),
    path('Login', LoginView.as_view(template_name='Logins/Login.html'), name='Login'),
    


]
