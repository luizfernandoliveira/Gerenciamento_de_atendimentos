from django.shortcuts import render


def cadastro_empresa(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_empresa.html', {'status': status})


def valida_cadastro_empresa(request):
    # nome = request.POST.get('nome')
    # tipo_contrato = request.POST.get('tipo_contrato')
    # data_de_cadastro = request.POST.get('data_de_cadastro')
    # data_final_contrato = request.POST.get('data_final_contrato')
    # responsavel_manutencao = request.POST.get('responsavel_manutencao')
    # telefone_responsavel = request.POST.get('telefone_responsavel')
    return


def lista_empresa():
    pass
