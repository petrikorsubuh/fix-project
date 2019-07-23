from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('test',ApiRespon.as_view()),
    path('users',ApiUsers.as_view()),
    path('dapils',ApiDapil.as_view()),
    path('account',ApiAccount.as_view()),
    path('partai',ApiPartai.as_view()),
    path('caleg',ApiCaleg.as_view()),
    path('kategori',ApiKategori.as_view()),
    path('kecamatan',ApiKecamatan.as_view()),
    path('kelurahan',ApiKelurahan.as_view()),
    path('suara',ApiSuara.as_view()),
]
