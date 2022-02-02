from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_empresa, name='cadastro_empresa'),
    path('lista/', views.lista_empresa, name='lista'),
    path('valida_cadastro_empresa/', views.valida_cadastro_empresa, name='valida_cadastro_empresa'),
]
