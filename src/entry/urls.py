#from django.conf.urls import patterns, url
from django.conf.urls import url, include
#from django.conf.urls.defaults import *

from .views import index, detail

app_name = 'entry'

urlpatterns = [
    url(r'^$', index, name='index'),
    # eg: /entries/5/
    url(r'^(?P<entry_id>\d+)/$', detail, name='detail'),
]
