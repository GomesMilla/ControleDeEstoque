from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  #Importando pacote Django padrão para recuperação de senha 


urlpatterns =[
   # SALAS
   path("Cadastrar-Sala", views.ViewCadastrarSala, name="ViewCadastrarSala"),




]