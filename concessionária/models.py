from django.db import models


class Concessionarias(models.Model):
    nome = models.CharField(max_length=100)
    contrato_suporte = models.BooleanField(default=False)
    tipo_contrato = models.CharField(max_length=30)
    data_final_contrato = models.DateField()
    responsavel_manutencao = models.CharField(max_length=30)
    telefone_responsavel = models.CharField(max_length=20)
