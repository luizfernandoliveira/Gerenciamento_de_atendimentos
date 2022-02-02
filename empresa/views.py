from django.shortcuts import render, redirect
from .models import Empresas


def cadastro_empresa(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_empresa.html', {'status': status})


def valida_cadastro_empresa(request):
    nome = request.POST.get('nome')
    tipo_contrato = request.POST.get('tipo_contrato')
    # data_de_cadastro = request.POST.get('data_de_cadastro')
    # data_final_contrato = request.POST.get('data_final_contrato')
    responsavel_manutencao = request.POST.get('responsavel_manutencao')
    telefone_responsavel = request.POST.get('telefone_responsavel')

    empresa = Empresas.objects.filter(nome=nome)

    try:
        empresa = Empresas(nome=nome,
                           tipo_contrato=tipo_contrato,
                           responsavel_manutencao=responsavel_manutencao,
                           telefone_responsavel=telefone_responsavel
                           )
        empresa.save()

        return redirect('/empresa/cadastro/?status=0')
    except Exception:
        return redirect('/empresa/cadastro/?status=1')


def lista_empresa():
    pass
