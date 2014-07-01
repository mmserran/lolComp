# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from compselector import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)