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
    path('display_ap', views.display_ap, name='display_ap'),
    path('display_powersupply', views.display_powersupply, name='display_powersupply'),
    path('edit_switch/<int:id>', views.edit_switch, name='edit_switch'),
    path('delete_switch', views.delete_switch, name='delete_switch'),
	]