import os.path

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

def basedir():
   """ Get the pwd of this module, eg for use setting absolute paths """
   return os.path.abspath(os.path.dirname(__file__))

urlpatterns = patterns('',
    ### django admin site
    (r'^admin/(.*)', admin.site.root),

    ### static media
    (r'^site_media/(.*)$',
     'django.views.static.serve',
     {'document_root': os.path.join(basedir(), 'media')}),

    ### main kegweg urls
    (r'', include('kegweb.kegweb.urls')),
)