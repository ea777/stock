from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
urlpatterns = [

    url("", index, name='index'),
    url(r'^admin/', admin.site.urls),



    url("display_switch/", display_switch, name='display_switch'),
    url(r"^display_Ap$", display_Ap, name='display_Ap'),
    url(r"^display_PowerSupply$", display_PowerSupply, name='display_PowerSupply'),

url(r"^add_switch$", add_switch, name='add_switch'),
url(r"^add_ap$", add_ap, name='add_ap'),
url(r"^add_power_supply$", add_power_supply, name='add_power_supply'),

# url(r"^edit_switch/(?P<pk>\d+$", edit_switch, name='edit_switch'),
# url(r"^edit_ap/(?P<pk>\d+$", edit_ap, name='edit_ap'),
# url(r"^edit_power_supply/(?P<pk>\d+$", edit_power_supply, name='edit_power_suppply'),
#
#
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_switch, name='delete_switch'),
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_power_supply, name='delete_power_supply'),
# url(r"^delete_power_supply/(?P<pk>\d+$", delete_ap, name='delete_ap'),
]