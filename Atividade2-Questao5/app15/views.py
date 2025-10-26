from django.shortcuts import render
from django.http import HttpResponse
def perfil(request,nome= None):
  if nome:
    return HttpResponse(f'<h1>Usuário: {nome}</h1>')
  else:
    return HttpResponse('<h1>Visitante</h1>')

