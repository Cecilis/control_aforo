# Generated by Django 2.2.13 on 2020-07-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacion',
            name='id_cliente',
            field=models.CharField(default='', max_length=255),
        ),
    ]
