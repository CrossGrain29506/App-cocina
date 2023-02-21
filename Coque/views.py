from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here. 
def hello(request):
 return render(request,'./index.html')

def login(request):
  return render(request,'./login.html') 

def reg(request):
  return render(request,'./reg.html')

#estos viws son de las comidas
def AusF(request):
  return render(request,'./AusF.html')

def FranF(request):
  return render(request,'./FranF.html')

def ItaliaF(request):
  return render(request,'./ItaliaF.html')

def JaponF(request):
  return render(request,'./JaponF.html') 

def MexF(request):
  return render(request,'./MexF.html')

def SpainF(request):
  return render(request,'./SpainF.html')   
  