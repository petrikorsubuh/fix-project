from django.contrib import admin
from django.urls import path

from apps.account import views

urlpatterns = [
    
    path('', views.IndexAccountView.as_view()),
    path('save', views.SaveAccountView.as_view()),
    path('edit/<int:id>', views.EditAccountView.as_view()),
    path('update', views.UpdateAccountView.as_view()),
    path('delete/<int:id>', views.DeleteAccountView.as_view()),
    path('tambah', views.TambahAccountView.as_view()),
]
