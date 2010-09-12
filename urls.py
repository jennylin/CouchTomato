from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Example:
    #(r'^challenge/', include('CouchTomato.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$','direct_to_template', {'template': 'index.htm'}),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
