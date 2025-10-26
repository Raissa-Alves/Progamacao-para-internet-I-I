from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def agenda(request,data):
  data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
  return HttpResponse(f'<h1>{data_formatada}</h1>')
