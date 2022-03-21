# Setting para configurar o Heroku para produção 

import environ

from main.settings.settings_local import * # Importando o settings local que é a base do settings

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

 # Domínio é o gratúito do Heroku por isso colocou como *, mas se fosse um domínio fixo colocava o domínio alí.
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}





