from django.contrib import admin
from django.urls import path

from apps.suara import views

urlpatterns = [
    path('',views.SuaraView.as_view()),
    path('tambah',views.TambahSuaraView.as_view()),
    path('save',views.SaveSuaraView.as_view()),
    path('edit/<int:id>',views.EditSuaraView.as_view()),
    path('update',views.UpdateSuaraView.as_view()),
    path('delete/<int:id>',views.DeleteSuaraView.as_view()),

    
]