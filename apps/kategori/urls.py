from django.contrib import admin
from django.urls import path

from apps.kategori import views

urlpatterns = [
    path('',views.IndexKategoriViews.as_view()),
    path('save',views.SaveKategoriView.as_view()),
    path('edit/<int:id>',views.EditKategoriView.as_view()),
    path('update',views.UpdateKategoriView.as_view()),
    path('delete/<int:id>',views.DeleteKategoriView.as_view()),
    path('tambah',views.TambahKategoriView.as_view()),

]
