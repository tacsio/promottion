#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('twitter.views',

	(r'^$', 'index'),
	(r'^search$', 'search'),
)
