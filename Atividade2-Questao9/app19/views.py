from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def site(request,dominio):
   return HttpResponseRedirect(f"https://{dominio}")