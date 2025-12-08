"""
URL configuration for HeartSafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('doctors/', views.doctors,name='doctors'),
    path('services/', views.services,name='services'),
    
    path('add_patient/', views.add_patient,name='add_patient'),
    path('add_symptom/', views.add_symptom,name='add_symptom'),     
    path('add_service/', views.add_service,name='add_service'),
    path('add_alert/', views.add_alert,name='add_alert'),
    path('payment/', views.payment,name='payment'),
]