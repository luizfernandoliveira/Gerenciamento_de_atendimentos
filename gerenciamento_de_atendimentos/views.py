from django.shortcuts import render
from atendimentos.models import Atendimento

def home(request):
    status = request.GET.get('status')
    return render(request, 'home.html', {'status': status})


def dashboard(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'dashboard.html', {'atendimentos': atendimentos})
