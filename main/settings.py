from pathlib import Path
import os, sys

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-6w23%li%v2=dkbe_#sahsag0zw*p96-o3nt4t@$_x$5$vgd-ak'

sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

# Configurações para programador e servidor local
DEBUG = False
ALLOWED_HOSTS = ['*'] # Domínio é o gratúito do Heroku por isso colocou como *, mas se fosse um domínio fixo colocava o domínio alí.


# Declarando aplicativos internos do Django
INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Declarando aplicativos externos do Django
INSTALLED_APPS += [
    'chartjs',
    'Usuarios',
    'Estoque',
    'Transacao',
    'easy_mask',
    'crispy_forms',
    'bootstrapform',
    'automated_logging',
    "view_breadcrumbs",
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'automated_logging.middleware.AutomatedLoggingMiddleware'
]


# AUTOMATED_LOGGING = {
#     "globals": {
#         "exclude": {
#             "applications": [
#                 "plain:contenttypes",
#                 "plain:admin",
#                 "plain:basehttp",
#                 "glob:session*",django_heroku.settings(locals())
#         "detailed_message": True,
#         "exclude": {"applications": [], "fields": [], "models": [], "unknown": False},
#         "loglevel": 20,
#         "mask": [],
#         "max_age": None,
#         "performance": False,
#         "snapshot": False,
#         "user_mirror": False,
#     },
#     "modules": ["request", "unspecified", "model"],
#     "request": {
#         "data": {
#             "content_types": ["application/json"],
#             "enabled": [],
#             "ignore": [],
#             "mask": ["password"],
#             "query": False,
#         },
#         "exclude": {
#             "applications": [],
#             "methods": ["GET"],
#             "status": [200],
#             "unknown": False,
#         },
#         "ip": True,
#         "loglevel": 20,
#         "max_age": None,
#     },
#     "unspecified": {
#         "exclude": {"applications": [], "files": [], "unknown": False},
#         "loglevel": 20,
#         "max_age": None,
#     },
# }


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Usuarios.views.Viewbase'
            ],
            'libraries':{
                'templatetag': 'Usuarios.templatetags.usuario_extras',
            }
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Configurações do Banco
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#Configurações para login declaração de user 
AUTH_USER_MODEL = "Usuarios.Pessoa" # Declarando nas configurações qual é o novo padrão de User
LOGIN_REDIRECT_URL = 'ViewIndex' # Redirecionando para a pagina inicial depois de logar
LOGIN_URL = 'ViewLogin' # Definindo a view padrão do Django de login


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configurações básicas

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#Definir a rota dos arquivos estaticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticFiles')

MEDIA_URL='/imagens/'
MEDIA_ROOT='imagens/'


# Configurações do Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Configurações de envio do e-mail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "gomesmillateste@gmail.com"
# EMAIL_HOST_PASSWORD = "GomesMillateste1"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "michel.lemes@unincor.edu.br"
EMAIL_HOST_PASSWORD = "87028399dd"

# Falta configurar para um email pessoal

