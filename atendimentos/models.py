from django.db import models
from django.contrib.auth.models import User
from empresa.models import Empresas # Importa o modelo da sua app empresas
from equipamento.models import Equipamento # Importa o modelo da sua app equipamentos

class Atendimento(models.Model):

    # Campos de escolha (usando tuplas para padronizar)
    STATUS_CHOICES = (
        ('Nao iniciado', 'Não iniciado'),
        ('Em andamento', 'Em andamento'),
        ('Aguardando retorno do cliente', 'Aguardando retorno do cliente'),
        ('Aguardando acesso ao servidor', 'Aguardando acesso ao servidor'),
        ('Concluido', 'Concluído'), # Adicionei este como sugestão
    )

    URGENCIA_CHOICES = (
        ('Urgente', 'Urgente'),
        ('Atencao', 'Atenção'),
        ('Moderado', 'Moderado'),
        ('Nao urgente', 'Não urgente'),
    )

    # O ID é gerado automaticamente pelo Django (ID serial)
    
    # Campo para o usuário logado
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Relacionamentos com outras apps
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.SET_NULL, null=True)

    # Campos de texto e data
    problema = models.CharField(max_length=200)
    descricao_detalhada = models.TextField()

    # Campos com opções de escolha
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Nao iniciado')
    urgencia = models.CharField(max_length=20, choices=URGENCIA_CHOICES, default='Moderado')
    
    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField()

    def __str__(self):
        return f'Atendimento #{self.id} - {self.problema}'

    # Opcional: Adicionar classe Meta para ordenar os atendimentos
    class Meta:
        ordering = ['-data_criacao']