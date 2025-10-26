from django.shortcuts import render
from django.http import HttpResponse 

def saudacao(request,nome):
    return HttpResponse(f'<h1>Óla, {nome} !</h1>') 