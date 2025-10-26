from django.shortcuts import render
from django.http import HttpResponse

def mostra_numero(request,num):
   return HttpResponse(f'<h1>Você digitou o número {num}</h1>')
