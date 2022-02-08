from django.contrib import admin
from .models import Empresas

# admin.site.register(Empresas)
# readonly_fields = ('nome', 'tipo contrato', 'data de cadastro',
#                        'data final contrato', 'responsavel manutencao', 'telefone responsavel')


@admin.register(Empresas)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'tipo_contrato', 'data_de_cadastro', 'data_final_contrato',
                       'responsavel_manutencao', 'telefone_responsavel')
