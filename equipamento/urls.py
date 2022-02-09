from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_equipamento/', views.cadastro_equipamento, name='cadastro_equipamento'),
    path('valida_cadastro_equipamento/', views.valida_cadastro_equipamento, name='valida_cadastro_equipamento'),
]
