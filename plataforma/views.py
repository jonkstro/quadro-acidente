from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .utils import cadastro_is_valid, lista_is_valid
from .models import Acidente
from django.contrib import messages
from django.contrib.messages import constants

hoje = datetime.now().date()

# Create your views here.
def quadro(request):
    data_max = Acidente.objects.latest('data').data
    dias_sem_acidente = hoje - data_max
    return render(request, 'quadro.html', {'dias':dias_sem_acidente.days})
    #return HttpResponse()
def cadastrar_acidente(request):
    data = request.POST.get('dataAcidente')
    local = request.POST.get('localAcidente')
    nome_funcionario = request.POST.get('nomeFuncionario')
    # return render(request, 'cadastrar_acidente.html')
    if request.method == 'GET':
        return render(request, 'cadastrar_acidente.html')
    if cadastro_is_valid(request, data, local, nome_funcionario):
    # se a data que for cadastrar for no futuro não é pra cadastrar:
        dt_obj = datetime.strptime(data, f'%Y-%m-%d').date()
        if dt_obj <= hoje:
            acidente = Acidente(
                data = data,
                local = local,
                nome_funcionario = nome_funcionario,
            )
            acidente.save()
            messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')
            return redirect('/quadro/')
        else:
            messages.add_message(request, constants.ERROR, 'Data se encontra no futuro')
            return redirect('/cadastrar_acidente/')
    else:
        return redirect('/cadastrar_acidente')
def listar_acidente(request):
    data_inicial = request.POST.get('dataInicial')
    data_final = request.POST.get('dataFinal')
    if lista_is_valid(request, data_inicial, data_final):
        #acidentes = Acidente.objects.all().order_by('data')
        acidentes = Acidente.objects.filter(data__range = [data_inicial, data_final]).order_by('data')
        return render(request, 'listar_acidente.html', {'acidentes': acidentes})
    else:
        return redirect('/listar_acidente/') 