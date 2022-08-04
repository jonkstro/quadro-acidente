from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def quadro(request):
    hoje = date.today()
    return render(request, 'quadro.html', {'hoje':hoje})

def cadastrar_acidente(request):
    return render(request, 'cadastrar_acidente.html')

def listar_acidente(request):
    return render(request, 'listar_acidente.html')