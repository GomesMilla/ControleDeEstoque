from Usuarios.models import Pais
import requests

"""
Docker
sudo docker-compose exec web python manage.py shell

Virtual Env
python manage.py shell

exec(open('apps/Scripts/Paises.py').read())
"""

def Pais():
    request = request.get("https://servicodados.ibge.gov.br/api/v1/paises/{paises}")
    for pais in request:
        print(request)
