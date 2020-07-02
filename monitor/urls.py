# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from monitor import views

urlpatterns = [
    path('', views.show, name='show'),
    path('agregar', views.monitor, name='monitor'),
    path('monitorURL', views.monitor_url),
    path('todos', views.todos),
    path('editar/<int:id>/', views.editar),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<int:id>/', views.actualizar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
]