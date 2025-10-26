from django.shortcuts import render
from django.http import HttpResponse 

def pedido (request,produto):
    return HttpResponse(f'Seus pedidos: {produto}')
