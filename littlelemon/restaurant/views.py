from django.shortcuts import render

# Create your views here.
from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
]