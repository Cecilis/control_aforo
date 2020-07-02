# Generated by Django 2.2.13 on 2020-06-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mac_wifi', models.CharField(default='', max_length=30)),
                ('mac_bluetooth', models.CharField(default='', max_length=30)),
                ('id_camara_zona', models.CharField(default='', max_length=300)),
                ('orientacion_display', models.CharField(default='H', max_length=1)),
                ('color_barra_cabecera', models.CharField(choices=[('WTH', 'Blanco'), ('G30', 'Gris 30'), ('G60', 'Gris 60'), ('BLK', 'Negro')], default='WTH', max_length=3)),
                ('logotipo', models.CharField(default='NO', max_length=300)),
                ('logotipo_posicion', models.CharField(choices=[('CTR', 'Centro'), ('RGT', 'Derecha'), ('LFT', 'Izquierda')], default='RGT', max_length=3)),
                ('fondo_imagen', models.CharField(default='NO', max_length=300)),
                ('aforo_formato', models.CharField(choices=[('PCT', 'Porcentaje'), ('RGT', 'Número')], default='RGT', max_length=3)),
                ('aforo_mostrar_maximo', models.BooleanField(default=False)),
                ('aforo_mostrar_casi_lleno', models.BooleanField(default=False)),
                ('aforo_frase_verde', models.CharField(default='', max_length=150)),
                ('aforo_frase_ambar', models.CharField(default='', max_length=150)),
                ('aforo_frase_rojo', models.CharField(default='', max_length=150)),
                ('monitor_estado', models.BooleanField(default=True)),
            ],
        ),
    ]
