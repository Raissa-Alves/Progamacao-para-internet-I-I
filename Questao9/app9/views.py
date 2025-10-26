from django.shortcuts import render
from django.http import HttpResponse

def download(request,nome,ext):
   return HttpResponse(f'<h1>Baixando: {nome}.{ext}</h1>')

