from django.contrib import admin
from django.urls import path

from apps.account import views

urlpatterns = [
    
    path('', views.IndexAccountView.as_view()),
    path('save', views.SaveAccountView.as_view(),name='save'),
    path('edit/<int:id>', views.EditAccountView.as_view(),name='edit'),
    path('update', views.UpdateAccountView.as_view(),name='update'),
    path('delete/<int:id>', views.DeleteAccountView.as_view(),name='delete'),
    path('tambah', views.TambahAccountView.as_view(),name='tambah'),
]
