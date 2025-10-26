from django.shortcuts import render
from django.http import HttpResponse

def artigo(request,slug):
  return HttpResponse(f'<h1>{slug}</h1>')

