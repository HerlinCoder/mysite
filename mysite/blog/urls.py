# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from blog import views
app_name='blog'
urlpatterns=[
	url(r'^$', views.index, name='index'),
]