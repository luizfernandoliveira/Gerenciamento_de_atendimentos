from django.db import models
from datetime import date


class Concessionarias(models.Model):
    nome = models.CharField(max_length=100, )
    contrato_suporte = models.BooleanField(default=False)
    tipo_contrato = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(default=date.today)
    data_final_contrato = models.DateField(verbose_name=None, blank=True, null=True)
    responsavel_manutencao = models.CharField(max_length=30, blank=True)
    telefone_responsavel = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'Concessionaria'

    def __str__(self):
        return self.nome
