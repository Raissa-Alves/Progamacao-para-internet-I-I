from django.shortcuts import render
from django.http import HttpResponse

def arquivo(request,nome,ext):
  return HttpResponse(f'<h1> {nome}.{ext}</h1>')
