from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here. 
def hello(request):
 return render(request,'./index.html')

def login(request):
  return render(request,'./account/login.html') 

def reg(request):
  return render(request,'./reg.html')

#vistas para las recetas en paises
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
#Spain
def RecetaTE(request):
  return render(request,'./RecetaTE.html')

def RecetaG(request):
  return render(request,'./RecetaG.html')

def RecetaCO(request):
  return render(request,'./RecetaCO.html')
#Australia
def RecetaAP(request):
  return render(request,'./RecetaAP.html')

def RecetaBA(request):
  return render(request,'./RecetaBA.html') 

def RecetaBB(request):
  return render(request,'./RecetaBB.html') 
#Francia
def RecetaPV(request):
  return render(request,'./RecetaPV.html')  

def RecetaRAT(request):
  return render(request,'./RecetaRAT.html')  

def RecetaCB(request):
  return render(request,'./RecetaCB.html')  
#Italia
def RecetaPIM(request):
  return render(request,'./RecetaPIM.html')

def RecetaRM(request):
  return render(request,'./RecetaRM.html')

def RecetaSC(request):
  return render(request,'./RecetaSC.html')
#Japon
def RecetaSUS(request):
  return render(request,'./RecetaSUS.html')

def RecetaON(request):
  return render(request,'./RecetaON.html')

def RecetaTEMP(request):
  return render(request,'./RecetaTEMP.html')  
#Mexico
def RecetaCP(request):
  return render(request,'./RecetaCP.html')

def RecetaMO(request):
  return render(request,'./RecetaMO.html')

def RecetaPOZ(request):
  return render(request,'./RecetaPOZ.html')
  


                              
         