from django.shortcuts import render
from django.http import HttpResponse 

def data(request,ano,mes):
    if mes >= 1 and mes <= 12:
       return HttpResponse(f'<h1>Ano:{ano}, Mês:{mes}</h1>')
    else:
        return HttpResponse('Erro: mês invalido') 
