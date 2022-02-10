# Arquivo para fazer a chamada para API
from Usuarios.models import Pais
import os
import requests #ele quem fará a requisição da API

def cadastrar_Paises():
    url = 'https://servicodados.ibge.gov.br/api/v1/paises/{paises}'
    paises = requests.get(url).json()
    for pais in paises:
        # objPais = Pais()
        # objPais.nome = pais.nome
        # objPais.sigla = pais.abreviado
        # objPais.save()

cadastrar_Paises()