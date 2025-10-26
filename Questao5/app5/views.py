from django.shortcuts import render
from django.http import HttpResponse 

def perfil(request,nome = None):
   if nome:
     return HttpResponse(f'<h1>Perfil de {nome}</h1>')
   else:
     return HttpResponse('<h1>Perfil de visitante.<h1>') 

