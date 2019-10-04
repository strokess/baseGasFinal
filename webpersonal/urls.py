"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from core import views # importamos el modulo views de core

urlpatterns = [
    path('',views.login, name="login"),
    path('visitas/',views.visitas, name="visitas"), #Manda a llamar la función que se creo en views con el nombre de home
    # en las comillas indicamos que es la raiz
    path('visitas2/',views.visitas2, name="visitas2"),
    path('clientes/', views.clientes, name="clientes"),
    path('compras/', views.compras, name="compras"),
    path('ventas/', views.ventas, name="ventas"),
    path('reportes/', views.reportes, name="reportes"),
    path('admin/', admin.site.urls),
]
