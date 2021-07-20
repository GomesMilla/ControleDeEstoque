from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuarios.urls')), #Incluindo a rota da Url criada no aplicativo url

]
