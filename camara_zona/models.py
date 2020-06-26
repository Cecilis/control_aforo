from djongo import models
from django import forms


class CamaraZona(models.Model):
    id = models.AutoField(primary_key=True)
    id_camara_zona = models.CharField(max_length=255, blank=False, default='')
    descripcion = models.CharField(max_length=250, blank=False, default='')
    camara_zona_estado = models.BooleanField(blank=False, default=True)

    class Meta:
        abstract = True
