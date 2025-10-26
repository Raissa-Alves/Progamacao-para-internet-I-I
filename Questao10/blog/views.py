from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Bem vindo ao GoodReads</h1> <p>O que é o GoodReads</p> <p>Como usar o GoodReads</p> ')

def post(request,ano,slug):
  return HttpResponse(f'<h1>{slug}</h1> <p>{ano}</p>')

def autor(request,nome):
   return HttpResponse(f'<h1>Como usar o GoodReads</h1> <p>escrito por:{nome}</p>')