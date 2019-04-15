from django.contrib import admin
from django.urls import path

from apps.partai import views

urlpatterns = [
    path('',views.IndexPartaiView.as_view()),
    path('save',views.SavePartaiView.as_view()),
    path('edit/<int:id>',views.EditPartaiView.as_view()),
    path('update/',views.UpdatePartaiView.as_view()),
    path('delete/<int:id>',views.DeletePartaiView.as_view()),
    path('tambah',views.TambahPartaiView.as_view()),
    path('service',views.PartaiService.as_view()),
    
]
