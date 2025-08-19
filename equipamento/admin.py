from django.contrib import admin
from .models import Equipamento


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('numero_equipamento', 'rodovia')
