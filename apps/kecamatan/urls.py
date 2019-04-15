from django.contrib import admin
from django.urls import path

from apps.kecamatan import views

urlpatterns = [
    path('',views.KecamatanView.as_view()),
    path('save',views.SaveKecamatanView.as_view()),
    path('edit/<int:id>',views.EditKecamatanView.as_view()),
    path('update',views.UpdateKecamatanView.as_view()),
    path('delete/<int:id>',views.DeleteKecamatanView.as_view()),
    path('tambah',views.TambahKecamatanView.as_view()),
    path('service',views.KecamatanService.as_view()),
    
]
