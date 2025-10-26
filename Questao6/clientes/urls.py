from django.contrib import admin
from django.urls import path
from clientes import views 

urlpatterns = [

    path('perfil/<str:nome>/', views.clientePerfil, name='clientePerfil')
]





