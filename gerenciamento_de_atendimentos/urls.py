"""gerenciamento_de_atendimentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('home/', views.home, name='home'),
    path('', RedirectView.as_view(url='/home/')),
    path('empresa/', include('empresa.urls')),
    path('empresa/', RedirectView.as_view(url='/empresa/cadastro_empresa/')),
    path('equipamento/', include('equipamento.urls')),
    path('equipamento/', RedirectView.as_view(url='/equipamento/cadastro_equipamento/')),
    path('dashboard/', views.dashboard, name='dashboard'),
]
