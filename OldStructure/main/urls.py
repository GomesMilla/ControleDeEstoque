from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView 
from Usuarios import views
from django.conf import settings
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuarios.urls')), #Incluindo a rota da Url criada no aplicativo url
    path('Estoque/', include('Estoque.urls')),
    
    # URLS DE INICIO
    path('', views.ViewInicio, name="ViewInicio"),
    path('ObjetivosDoSistema', views.ViewObjetivos, name="ViewObjetivos"),
    path('PublicoAlvo', views.ViewPublicoAlvo, name="ViewPublicoAlvo"),
    path('login/', views.ViewLogin, name = 'ViewLogin'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    


]
