from django.urls import path
from django.conf.urls import url
from monitor import views

urlpatterns = [
    path('', views.monitor_fs, name='monitor'),
    path('monitorURL', views.monitor_url),
]