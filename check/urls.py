from django.contrib import admin
from django.urls import path
from check import views

urlpatterns = [
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("accept",views.accept,name='accept'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
]