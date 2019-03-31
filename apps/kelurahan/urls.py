from django.contrib import admin
from django.urls import path

from apps.kelurahan import views

urlpatterns = [
    path('',views.KelurahanViews.as_view()),
    path('save',views.SaveKelurahanView.as_view()),
    path('edit/<int:id>',views.EditKelurahanView.as_view()),
    path('update',views.UpdateKelurahanView.as_view()),
    path('delete/<int:id>',views.DeleteKelurahanView.as_view()),
    path('tambah',views.TambahKelurahanView.as_view()),
]