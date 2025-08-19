from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atendimentos, name='lista_atendimentos'),
    path('novo/', views.novo_atendimento, name='novo_atendimento'),
]