from django.db import models
from empresa.models import Empresas


class Equipamento(models.Model):
    numero_equipamento = models.CharField(max_length=30)
    rodovia = models.CharField(max_length=50)
    km = models.CharField(max_length=10)
    sentido = models.CharField(max_length=30)
    ip = models.CharField(max_length=15, blank=True)
    mascara = models.CharField(max_length=15, blank=True)
    gateway = models.CharField(max_length=15, blank=True)
    ip_buffer = models.CharField(max_length=15, blank=True)

    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
