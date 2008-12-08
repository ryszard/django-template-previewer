from django.conf.urls.defaults import *
from django.conf import settings
from views import template_with_fix

urlpatterns = patterns('',
                       (r'^template/(?P<template>.*\.html)$', template_with_fix),
                       (r'^template/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_DIRS[0] , 'show_indexes': True}),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       )
