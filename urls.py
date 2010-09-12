from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Example:
    #(r'^challenge/', include('CouchTomato.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$','django.views.generic.simple.direct_to_template', {'template': 'index.htm'}),
    (r'^category/(?P<category>\w+)/?$','django.views.generic.simple.direct_to_template', {'template': 'index.htm'}),
    (r'^graph/','django.views.generic.simple.direct_to_template', {'template': 'graph.htm'}),
    (r'^search/(?P<location>.*)/?$', 'CouchTomato.challenge.views.search'),
    (r'^search/(?P<category>\w+)/(?P<location>.*)/?$', 'CouchTomato.challenge.views.search_category'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
