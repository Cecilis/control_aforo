# -*- encoding: utf-8 -*-
from djongo import models
from instalacion.models import Instalacion


class CamaraZona(models.Model):
    _id = models.ObjectIdField()
    id_instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    id_camara_zona = models.CharField(max_length=255, blank=False, default='0')
    descripcion = models.CharField(max_length=250, blank=False, default='')
    camara_zona_estado = models.BooleanField(blank=False, default=True)
