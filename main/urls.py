from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView # Importando a View Login padrão do Django 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuarios.urls')), #Incluindo a rota da Url criada no aplicativo url
    path('', LoginView.as_view(template_name='Logins/Login.html'), name='Login'),

]
