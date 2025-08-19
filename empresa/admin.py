from django.contrib import admin
from .models import Empresas


@admin.register(Empresas)
class EmpresaAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'tipo_contrato', 'data_de_cadastro', 'data_final_contrato',
                       'responsavel_manutencao', 'telefone_responsavel')
