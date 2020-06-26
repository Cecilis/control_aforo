from djongo import models
from django import forms

from monitor.forms import MonitorForm
from monitor.models import Monitor
from camara_zona.forms import CamaraZonaForm
from camara_zona.models import CamaraZona

class Instalacion(models.Model):
    #_id = models.ObjectIdField()
    id = models.AutoField(primary_key=True)
    nombre_comercial = models.CharField(max_length=255, blank=False, default='')
    direccion = models.CharField(max_length=255, blank=False, default='')
    telefono = models.CharField(max_length=20, blank=False, default='')
    movil = models.CharField(max_length=20, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    poblacion = models.CharField(max_length=255, blank=False, default='')
    provincia = models.CharField(max_length=255, blank=False, default='')
    codigo_postal = models.CharField(max_length=10, blank=False, default='')
    contacto_nombre = models.CharField(max_length=255, blank=False, default='')
    contacto_cargo = models.CharField(max_length=255, blank=False, default='')
    contacto_telefono = models.CharField(max_length=20, blank=False, default='')
    contacto_movil = models.CharField(max_length=20, blank=False, default='')
    contacto_email = models.CharField(max_length=255, blank=False, default='')
    tecnico_nombre = models.CharField(max_length=255, blank=False, default='')
    tecnico_cargo = models.CharField(max_length=255, blank=False, default='')
    tecnico_telefono = models.CharField(max_length=20, blank=False, default='')
    tecnico_movil = models.CharField(max_length=20, blank=False, default='')
    tecnico_email = models.CharField(max_length=255, blank=False, default='')
    instalacion_estado = models.BooleanField(blank=False, default=True)


    monitores = models.ArrayField(
        model_container=Monitor,
        null=True,
        blank=True,
        model_form_class=MonitorForm,
    )

    camara_zonas = models.ArrayField(
        model_container=CamaraZona,
        null=True,
        blank=True,
        model_form_class=CamaraZonaForm,
    )

    objects = models.DjongoManager()