"""gerenciamento_de_atendimentos URL Configuration
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
    path('atendimentos/', include('atendimentos.urls')),
]
