from django.contrib import admin
from django.urls import path

from apps.tps import views

urlpatterns = [
    path('',views.IndexTpsView.as_view()),
    # path('save',views.SaveTpsView.as_view()),
    path('edit/<int:id>',views.EditTpsView.as_view()),
    path('update/',views.UpdateTpsView.as_view()),
    path('delete/<int:id>',views.DeleteTpsViews.as_view()),
    path('tambah',views.TambahTpsView.as_view()),
    
]
