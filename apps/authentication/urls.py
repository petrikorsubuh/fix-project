from django.contrib import admin
from django.urls import path

from apps.authentication import views

urlpatterns = [
    path('', views.LoginView.as_view()),
    path('process', views.LoginProccessView.as_view(), name='process'),
    
]