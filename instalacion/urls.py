from django.urls import path
from django.conf.urls import url
from instalacion import views

urlpatterns = [
    path('', views.instalacion, name='instalacion'),
    path('todos', views.todos),
    path('editar/<int:id>/', views.editar),
    path('actualizar/<int:id>/', views.actualizar),
    path('eliminar/<int:id>/', views.eliminar),
]