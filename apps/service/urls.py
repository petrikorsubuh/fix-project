from django.contrib import admin
from django.urls import path

from .views import TestRespon, TestUsers

urlpatterns = [
    path('test',TestRespon.as_view()),
    path('users',TestUsers.as_view()),
]
