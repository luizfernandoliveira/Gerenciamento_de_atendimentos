from django.shortcuts import render, redirect
from equipamento.models import Equipamento


def cadastro_equipamento(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_equipamento.html', {'status': status})


def valida_cadastro_equipamento(request):
    numero_equipamento = request.POST.get('numero_equipamento')
    rodovia = request.POST.get('rodovia')
    km = request.POST.get('km')
    sentido = request.POST.get('sentido')
    empresa = request.POST.get('empresa')
    ip = request.POST.get('ip')
    mascara = request.POST.get('mascara')
    gateway = request.POST.get('gateway')
    buffer = request.POST.get('buffer')

    # if len(nome_equipamento.strip() == 0) or len(rodovia.strip() == 0) or len(km.strip() == 0) or \
    #         (nome_equipamento.strip() == 0) or (sentido.strip() == 0) or (empresa.strip() == 0):
    #     return redirect('/equipamento/cadastro_equipamento/?status=0')

    # try:
    #     equipamento = Equipamento(numero_equipamento=numero_equipamento,
    #                               rodovia=rodovia,
    #                               km=km,
    #                               sentido=sentido,
    #                               empresa=empresa,
    #                               ip=ip,
    #                               mascara=mascara,
    #                               gateway=gateway,
    #                               buffer=buffer
    #                               )
    #
    #     equipamento.save()
    #
    #     return redirect('/equipamento/cadastro_equipamento/?status=1')
    #
    # except Exception:
    #     return redirect('/equipamento/cadastro_equipamento/?status=2')

    equipamento = Equipamento(numero_equipamento=numero_equipamento,
                              rodovia=rodovia,
                              km=km,
                              sentido=sentido,
                              # empresa=empresa,
                              ip=ip,
                              mascara=mascara,
                              gateway=gateway,
                              ip_buffer=buffer
                              )

    equipamento.save()
    return redirect('/equipamento/cadastro_equipamento/?status=1')
