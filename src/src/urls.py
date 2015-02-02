from django.conf.urls import patterns, include, url
from django.contrib import admin
from calTrack import views as ct_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',ct_views.index),
    url(r'^ajax/(\w+)/$',ct_views.loadAjaxData),
)
