from django.contrib import admin
from django.urls import path
from pedidos import views

urlpatterns = [ 
  path('user/<str:nome>/produto/<str:nome>/', views.pedido, name='pedido') 

]