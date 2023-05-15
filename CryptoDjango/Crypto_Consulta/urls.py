"""Crypto_Consulta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from Consultas.views import home_0
from Consultas.views import home
from Consultas.views import some_view
from Consultas.views import teste2
from Consultas import views as main_views
from django.db import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_0/', home_0),
    path('home/', some_view),
    #path('teste2/', main_views.teste2, name="teste2"),
    path('teste2/', teste2, name="teste2"),
]
