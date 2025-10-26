from django.shortcuts import render
from django.http import HttpResponse 

def clientePerfil(request,nome):
     return HttpResponse(f'<h1>Perfil de {nome}.<h1>') 

