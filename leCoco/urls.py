"""leCoco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from Coque import views
from django import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('index/', views.hello),
    path('login/', views.login),
    path('reg/',views.reg),
    path('AusF/',views.AusF),
    path('FranF/',views.FranF),
    path('ItaliaF/',views.ItaliaF),
    path('JaponF',views.JaponF),
    path('MexF/',views.MexF),
    path('SpainF/',views.SpainF),

    path('RecetaTE/',views.RecetaTE),
    path('RecetaG/',views.RecetaG),
    path('RecetaCO/',views.RecetaCO),

    path('RecetaAP/',views.RecetaAP),
    path('RecetaBA/',views.RecetaBA),
    path('RecetaBB/',views.RecetaBB),

    path('RecetaRAT/',views.RecetaRAT),
    path('RecetaPV/',views.RecetaPV),
    path('RecetaCB/',views.RecetaCB),

    path('RecetaPIM/',views.RecetaPIM),
    path('RecetaRM/',views.RecetaRM),
    path('RecetaSC/',views.RecetaSC),

    path('RecetaSUS/',views.RecetaSUS),
    path('RecetaTEMP/',views.RecetaTEMP),
    path('RecetaON/',views.RecetaON),

    path('RecetaCP/',views.RecetaCP),
    path('RecetaPOZ/',views.RecetaPOZ),
    path('RecetaMO/',views.RecetaMO),

    path('accounts/', include('allauth.urls')),

]
