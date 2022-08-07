#REALIZAR A VALIDAÇÃO DOS DADOS DE LOGIN E SENHA
import re
from django.contrib import messages
from django.contrib.messages import constants
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def cadastro_is_valid(request, data, local, nome):
    if data == '':
        messages.add_message(request, constants.ERROR, 'Preencha um valor de data válida')
        return False
    if local == '':
        messages.add_message(request, constants.ERROR, 'Preencha um valor de local válido')
        return False
    if nome == '':
        messages.add_message(request, constants.ERROR, 'Preencha um valor de nome válido')
        return False
    return True

def lista_is_valid(request, data_inicial, data_final):
    if data_inicial == '':
        messages.add_message(request, constants.ERROR, 'Preencha um valor de data válida')
        return False
    if data_final == '':
        messages.add_message(request, constants.ERROR, 'Preencha um valor de data válida')
        return False
    return True