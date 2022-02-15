from django.contrib.auth.models import Group

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

"""
Docker
sudo docker-compose exec web python manage.py shell

Virtual Env
python manage.py shell

exec(open('apps/Scripts/Groups.py').read())
"""

def validate(grupo):
    try:
        validar = Group.objects.get(name = grupo)
        if validar:
            return False
        else:
            return True
    except:
        return True

def registrar_grupos():
    listGrupos = ["Administrador", "Vendedor", "Gerente", "Financeiro", "Usuário"]
    print(BOLD + "\nFoi iniciado a geração de registros dos grupos!\n" + RESET)
    for nomeGrupo in listGrupos:
        if validate(nomeGrupo):
            Group.objects.create(name=nomeGrupo)
            print(GREEN + "O grupo" + RESET + BOLD + f" {nomeGrupo} " + RESET + GREEN + "foi registrado com sucesso no sistema!" + RESET)
        else:
            print(RED + "O grupo" + RESET + BOLD + f" {nomeGrupo} " + RESET + RED + "já está registrado no sistema!" + RESET)

registrar_grupos()
