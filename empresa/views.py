from django.shortcuts import render, redirect
from .models import Empresas


def cadastro_empresa(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_empresa.html', {'status': status})


def valida_cadastro_empresa(request):
    nome = request.POST.get('nome')
    tipo_contrato = request.POST.get('tipo_contrato')
    data_de_cadastro = request.POST.get('data_de_cadastro')
    data_final_contrato = request.POST.get('data_final_contrato')
    responsavel_manutencao = request.POST.get('responsavel_manutencao')
    telefone_responsavel = request.POST.get('telefone_responsavel')

    empresa = Empresas.objects.filter(nome=nome)

    if len(nome.strip()) == 0 or len(tipo_contrato.strip()) == 0 or len(data_de_cadastro.strip()) == 0 \
            or len(data_final_contrato.strip()) or len(responsavel_manutencao.strip()) \
            or len(telefone_responsavel.strip()):
        return redirect('/empresa/cadastro/?status=1')

    try:
        empresa = Empresas( nome=nome,
                            tipo_contrato=tipo_contrato,
                            data_de_cadastro=data_de_cadastro,
                            data_final_contrato=data_final_contrato,
                            responsavel_manutencao=responsavel_manutencao,
                            telefone_responsavel=telefone_responsavel)
        empresa.save()

        return redirect(('/empresa/cadastro/?status=0'))
    except(Exception):
        return redirect('/auth/cadastro/?status=4')


def lista_empresa():
    pass
