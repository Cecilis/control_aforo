from djongo import models
from django import forms

from instalacion.forms import InstalacionForm
from instalacion.models import Instalacion

class Cliente(models.Model):
    #_id = models.ObjectIdField()
    id = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=20, blank=False, default='')
    razon_social = models.CharField(max_length=255, blank=False, default='')
    direccion = models.CharField(max_length=255, blank=False, default='')
    poblacion = models.CharField(max_length=255, blank=False, default='')
    provincia = models.CharField(max_length=255, blank=False, default='')
    codigo_postal = models.CharField(max_length=10, blank=False, default='')
    telefono = models.CharField(max_length=20, blank=False, default='')
    movil = models.CharField(max_length=20, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    administracion_nombre = models.CharField(max_length=255, blank=False, default='')
    administracion_cargo = models.CharField(max_length=255, blank=False, default='')
    administracion_telefono = models.CharField(max_length=20, blank=False, default='')
    administracion_movil = models.CharField(max_length=20, blank=False, default='')
    administracion_email = models.CharField(max_length=255, blank=False, default='')
    tecnico_nombre = models.CharField(max_length=255, blank=False, default='')
    tecnico_cargo = models.CharField(max_length=255, blank=False, default='')
    tecnico_telefono = models.CharField(max_length=20, blank=False, default='')
    tecnico_movil = models.CharField(max_length=20, blank=False, default='')
    tecnico_email = models.CharField(max_length=255, blank=False, default='')
    cliente_estado= models.BooleanField(blank=False, default=True)

    objects = models.DjongoManager()