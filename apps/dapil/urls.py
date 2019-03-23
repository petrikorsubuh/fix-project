from django.contrib import admin
from django.urls import path

from apps.dapil import views

urlpatterns = [
    path('',views.DapilView.as_view()),
    path('save',views.SaveDapilView.as_view()) ,
    path('edit/<int:id>',views.EditDapilView.as_view()) ,
    path('update',views.UpdateDapilView.as_view()) ,
    path('delete/<int:id>',views.DeleteDapilView.as_view()) ,
    path('tambah',views.TambahDapilView.as_view()) ,

]
