# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-25 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0027_auto_20171225_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='procedure',
            field=models.CharField(choices=[('ipu', 'ipu'), ('entropy', 'entropy')], default='ipu', max_length=50, verbose_name='Procedure'),
        ),
    ]
