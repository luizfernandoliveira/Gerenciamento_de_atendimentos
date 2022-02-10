from django.db import models
from empresa.models import Empresas


class Equipamento(models.Model):
    numero_equipamento = models.CharField(max_length=30)
    rodovia = models.CharField(max_length=50)
    km = models.CharField(max_length=10)
    sentido = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    mascara = models.CharField(max_length=15, blank=True, null=True)
    gateway = models.CharField(max_length=15, blank=True, null=True)
    ip_buffer = models.CharField(max_length=15, blank=True, null=True)
    # empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.numero_equipamento     # utiliza o numero do equipamento no admin para listar
