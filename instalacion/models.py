# -*- encoding: utf-8 -*-
from djongo import models
from django import forms

from cliente.models import Cliente

class Instalacion(models.Model):
    _id = models.ObjectIdField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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

