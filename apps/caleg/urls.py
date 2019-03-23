from django.contrib import admin
from django.urls import path

from apps.caleg import views

urlpatterns = [
    path('',views.CreateCalegView.as_view()),
    path('save',views.SaveCalegView.as_view()),
    path('edit/<int:id>',views.EditCalegView.as_view()),
    path('update',views.UpdateCalegView.as_view()),
    path('delete/<int:id>',views.DeleteCalegView.as_view()),
    path('tambah',views.TambahCalegView.as_view()),

]
