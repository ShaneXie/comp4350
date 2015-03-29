from django.conf.urls import patterns, include, url
from django.contrib import admin
from calTrack import views as ct_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',ct_views.index),
    url(r'^ajax/(\w+)/$',ct_views.loadAjaxData),
    url(r'^api/(\w+)/$',ct_views.loadJSON),
)
