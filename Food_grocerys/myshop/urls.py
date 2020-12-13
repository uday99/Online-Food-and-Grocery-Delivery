"""Food_grocerys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myshop import views

urlpatterns = [
    path('',views.showIndex,name='main'),
    path('register/',views.register,name='register'),
    path('user-otp',views.userOtp,name='user-otp'),
    path('validate_otp/',views.validateOTp,name='validate_otp'),
    path('confirmation/',views.confirmation,name='confirmation'),

    path('login/',views.loginPage,name='login')

]
