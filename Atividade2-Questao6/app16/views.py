from django.shortcuts import render
from django.http import HttpResponse

def email(request,email):
 try:
  return HttpResponse(f'<h1>{email}</h1>')
 except ValueError:
  return HttpResponse(f'<h1>email inválido</h1>')