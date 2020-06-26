from djongo import models
from django import forms


class Monitor(models.Model):
    WHITE = 'WTH'
    GREY30 = 'G30'
    GREY60 = 'G60'
    BLACK = 'BLK'
    HEADER_COLOR = (
        (WHITE, 'Blanco'),
        (GREY30, 'Gris 30'),
        (GREY60, 'Gris 60'),
        (BLACK, 'Negro'),
    )

    CENTER = 'CTR'
    RIGHT = 'RGT'
    LEFT = 'LFT'
    LOGO_ALIGN = (
        (CENTER, 'Centro'),
        (RIGHT, 'Derecha'),
        (LEFT, 'Izquierda'),
    )

    PERCENT = 'PCT'
    NUMBER = 'RGT'

    CAPACITY = (
        (PERCENT, 'Porcentaje'),
        (NUMBER, 'Número'),
    )

    id = models.AutoField(primary_key=True)
    mac_wifi = models.CharField(max_length=30, blank=False, default='')
    mac_bluetooth = models.CharField(max_length=30, blank=False, default='')
    id_camara_zona = models.CharField(max_length=300, blank=False, default='')
    orientacion_display = models.CharField(max_length=1, blank=False, default='H')
    color_barra_cabecera = models.CharField(max_length=3, choices=HEADER_COLOR, default=WHITE)
    logotipo = models.CharField(max_length=300, blank=False, default='NO')
    logotipo_posicion = models.CharField(max_length=3, choices=LOGO_ALIGN, default=RIGHT)
    fondo_imagen = models.CharField(max_length=300, blank=False, default='NO')
    aforo_formato = models.CharField(max_length=3, choices=CAPACITY, default=NUMBER)
    aforo_mostrar_maximo = models.BooleanField(blank=False, default=False)
    aforo_mostrar_casi_lleno = models.BooleanField(blank=False, default=False)
    aforo_frase_verde = models.CharField(max_length=150, blank=False, default='')
    aforo_frase_ambar = models.CharField(max_length=150, blank=False, default='')
    aforo_frase_rojo = models.CharField(max_length=150, blank=False, default='')
    monitor_estado = models.BooleanField(blank=False, default=True)

    class Meta:
        abstract = True
