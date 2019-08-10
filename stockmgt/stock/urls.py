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
    path('display_accesspoint', views.display_accesspoint, name='display_accesspoint'),
    path('display_powersupply', views.display_powersupply, name='display_powersupply'),
    path('edit_switch/<int:id>', views.edit_switch, name='edit_switch'),
    path('edit_accesspoint/<int:id>', views.edit_accesspoint, name='edit_accesspoint'),
    path('edit_powersupply/<int:id>', views.edit_powersupply, name='edit_powersupply'),
    path('delete_switch_complete/<int:id>', views.delete_switch, name='delete_switch'),
    path('delete_accesspoint_complete/<int:id>', views.delete_accesspoint, name='delete_accesspoint'),
    path('delete_powersupply_complete/<int:id>', views.delete_powersupply, name='delete_powersupply'),

]