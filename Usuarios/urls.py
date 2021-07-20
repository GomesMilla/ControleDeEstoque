from django.urls import path
from .views import *


urlpatterns =[
    path('Criar-Conta/', ViewCriarConta, name="ViewCriarConta"),
    path('Início/', ViewIndex, name="ViewIndex"),

]