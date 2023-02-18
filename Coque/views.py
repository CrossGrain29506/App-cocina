from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here. 
def hello(request):
 return render(request,'./index.html')

def login(request):
  return render(request,'./login.html') 