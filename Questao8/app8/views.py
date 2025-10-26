from django.shortcuts import render
from django.http import HttpResponse

def produto(request,categoria,nome):
  return HttpResponse(f'<h1>Produto:{nome}, Categoria: {categoria}</h1>')

