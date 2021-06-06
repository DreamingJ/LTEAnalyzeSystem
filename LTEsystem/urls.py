"""LTEsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('index/', views.index),
    path('login/', views.login),
    path('adminlogin/', views.adminlogin),
    path('register/', views.register),
    path('logout/', views.logout),
    path('adminlogout/', views.adminlogout),
    path('main/', views.main),
    path('manager/', views.manager),
    path('datamanage/', views.datamanage),
    path('datamanage/import', views.importdata),
    path('datamanage/export', views.exportdata),
    path('conmanage/', views.connectmanage),
    path('conmanage/initframe/', views.initframe),
    path('conmanage/cate1/', views.infocate1),
    path('conmanage/cate2/', views.infocate2),
    path('conmanage/cate3/', views.infocate3),
    path('infoquery/', views.info_query),
    path('infoquery/cell/', views.cell_info),
    path('infoquery/enodeb/', views.enodeb_info),
    path('infoquery/kpi/', views.kpi_info),
    path('infoquery/prb/', views.prb_info),
    path('analyze/', views.analyze1),
]
