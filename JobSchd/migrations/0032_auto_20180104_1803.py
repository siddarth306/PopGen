# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0031_auto_20180103_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_geo',
            field=models.CharField(default='sample_geo', help_text='TAZ', max_length=50, verbose_name='Disaggregate Spatial Unit'),
        ),
    ]