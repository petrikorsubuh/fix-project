from django.contrib import admin
from django.urls import path

from apps.suara import views

urlpatterns = [
    path('tambah',views.TambahSuaraView.as_view()),
    path('',views.SuaraView.as_view()),
    path('save',views.SaveSuaraView.as_view()),
    
]