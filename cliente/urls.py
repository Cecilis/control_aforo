# -*- encoding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from cliente import views

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('mng', views.mng, name='mng'),
    path('todos', views.todos),
    path('editar/<int:id>/', views.editar),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<int:id>/', views.actualizar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar),
]