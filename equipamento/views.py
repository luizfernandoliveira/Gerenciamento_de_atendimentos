from django.shortcuts import render


def cadastro_equipamento(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_equipamento.html', {'status': status})


def valida_cadastro_equipamento(request):
    pass
