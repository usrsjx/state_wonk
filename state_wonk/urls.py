from django.conf.urls import patterns, include, url
from django.contrib import admin

from state_data import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', views.view_map, name='view_map'),
)
