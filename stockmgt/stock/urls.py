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
    path('display_powersupply', views.display_PowerSupply, name='display_powersupply'),

    # url(r"^display_ap/$", display_Ap, name='display_Ap'),
    # url(r"^display_powersupply/$", display_PowerSupply, name='display_PowerSupply'),

# url(r"^add_switch$", add_switch, name='add_switch'),
# url(r"^add_ap$", add_ap, name='add_ap'),
# url(r"^add_power_supply$", add_power_supply, name='add_power_supply'),

# url(r"^edit_switch/(?P<pk>\d+$", edit_switch, name='edit_switch'),
# url(r"^edit_ap/(?P<pk>\d+$", edit_ap, name='edit_ap'),
# url(r"^edit_power_supply/(?P<pk>\d+$", edit_power_supply, name='edit_power_suppply'),
#
#
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_switch, name='delete_switch'),
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_power_supply, name='delete_power_supply'),
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_ap, name='delete_ap'),
]