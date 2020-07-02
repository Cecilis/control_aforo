# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import url, include
from django.urls import path, re_path
from app import views

urlpatterns = [

    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),

    # full screen horizontal monitor view
    path('hfs', views.hfs, name='hfs'),

    # The home page
    path('', views.index, name='home'),

    path('api/', include('monitor.urls')),
    path('monitor/', include('monitor.urls')),
    path('camara_zona/', include('camara_zona.urls')),
    path('cliente/', include('cliente.urls')),
    path('instalacion/', include('instalacion.urls')),


]
