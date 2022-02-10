from django.contrib import admin
from .models import Equipamento


@admin.register(Equipamento)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('numero_equipamento', 'rodovia')
