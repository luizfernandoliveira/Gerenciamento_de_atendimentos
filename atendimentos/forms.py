from django import forms
from .models import Atendimento

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'
        widgets = {
            'problema': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Problema...'}),
            'descricao_detalhada': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'urgencia': forms.Select(attrs={'class': 'form-control'}),
            'data_atendimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Você pode querer esconder o campo de ID, pois ele é gerado automaticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'id' in self.fields:
            self.fields['id'].widget = forms.HiddenInput()