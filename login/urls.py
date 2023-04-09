from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include
from.import views

urlpatterns = [

    path('register/', views.register, name="register"),
    # path('login/', views.LoginPage,name='login'),
    path('home/', views.HomePage, name='home'),
    path('home/login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('home/dashboard/', views.dashboard, name='dashboard'),


]