from django.conf.urls.defaults import *
from django.conf import settings
from django.views.decorators.cache import never_cache

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
    (r'^search/(?P<location>.+)/(?P<term>.*)/?$', 'CouchTomato.challenge.views.search'),
    (r'^search/(?P<location>.+)/(?P<category>\w*)/()?P<term>.*/?$', 'CouchTomato.challenge.views.search_category'),
    (r'^category/(?P<category>\w+)/?$','django.views.generic.simple.direct_to_template', {'template': 'index.htm'}),
    (r'^graph/','django.views.generic.simple.direct_to_template', {'template': 'graph.htm'}),
    (r'^$/','django.views.generic.simple.direct_to_template', {'template': 'index.htm'}),
    (r'^couch/','django.views.generic.simple.direct_to_template', {'template': 'index.htm'}),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
