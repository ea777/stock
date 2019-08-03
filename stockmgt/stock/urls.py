from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
admin.autodiscover()
urlpatterns = [

    url(r'^$', views.index, name='index'),





    path('display_switch', views.display_switch, name='display_switch'),
    path('display_accesspoint', views.display_Ap, name='display_accesspoint'),
    path('display_powersupply', views.display_PowerSupply, name='display_powersupply')
	]