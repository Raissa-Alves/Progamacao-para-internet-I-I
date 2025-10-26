from django.shortcuts import render
from django.http import HttpResponse 

def soma(request,a,b):
  ResultSoma = a + b
  return HttpResponse(f'<h1>Resultado: {ResultSoma}</h1>')
      
