from django.shortcuts import render, redirect
from .models import Atendimento
from .forms import AtendimentoForm

def lista_atendimentos(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'atendimentos/lista.html', {'atendimentos': atendimentos})

def novo_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoForm()
    return render(request, 'atendimentos/novo.html', {'form': form})