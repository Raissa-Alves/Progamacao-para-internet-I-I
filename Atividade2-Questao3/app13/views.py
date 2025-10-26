from django.shortcuts import render
from django.http import HttpResponse

def usuario(request,nome,idade):
    return HttpResponse(f'<h1>{nome} tem {idade} anos!</h1>')