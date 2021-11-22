"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',inicio, name="inicio" ),
    path('fav-miami/',miami, name="miami"),
    path("fav-barranquilla/", barranquilla, name="barranquilla"),
    path("fav-paris", paris, name="paris"),  
    path("fav-medellin", medellin, name="medellin"),
    path("programar", programar, name="programar"),  
    path("planear", planear, name="planear"),
    path("agregar", agregar, name="agregar"),
    path('editar<int:id>', editar, name='editar'),
    path('eliminar<int:id>', eliminar, name='eliminar'),
    path('registrarce/',registrar_user, name='registrarce'),
    path('ingresar/',ingresar, name='ingresar'),
    path('salir/',salir, name='salir'),
    path('covid-19/',noticias, name='covid-19'),
    path('paquetes/',paquetes, name='paquetes'),
    
]
