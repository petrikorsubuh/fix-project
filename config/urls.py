"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.build import views
# from apps.dapil import views as views_dapil
# from apps.account import views as views_account
from apps.authentication import views as views_aut
from config.views import Index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Index.as_view() ),
    path('admin/', admin.site.urls),
    path('index', views.IndexView.as_view()),
    path('language/save', views.SaveLanguageView.as_view()),
    path('language/edit/<int:id>', views.EditLanguageView.as_view()),
    path('language/update', views.UpdateLanguageView.as_view()),
    path('language/delete/<int:id>', views.DeleteLanguageView.as_view()),


    path('dapil/', include(('apps.dapil.urls', 'dapil'), namespace='dapil')),
    path('kecamatan/', include(('apps.kecamatan.urls', 'kecamatan'), namespace='kecamatan')),
    path('kelurahan/', include(('apps.kelurahan.urls', 'kelurahan'), namespace='kelurahan')),
    path('kategori/',include(('apps.kategori.urls','kategori'),namespace='kategori')),
    path('caleg/',include(('apps.caleg.urls','caleg'),namespace='caleg')),
    path('tps/',include(('apps.tps.urls','tps'),namespace='tps')),
    path('partai/',include(('apps.partai.urls','partai'),namespace='partai')),
    path('account/',include(('apps.account.urls','account'),namespace='account')),
    
    
    
    path('suara/',include(('apps.suara.urls','suara'),namespace='suara')),


    #relawan
    path('relawan/',include(('apps.user.urls','user'),namespace='relawan')),
    
    path('api/',include(('apps.service.urls','service'),namespace='service')),

    # login
    path('login/', include(('apps.authentication.urls', 'login'), namespace='login')),
    path('logout/', views_aut.LogOutView.as_view(), name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
