# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0006_job_houseen'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='PersonEN',
            field=models.CharField(default='asfasd', max_length=50),
            preserve_default=False,
        ),
    ]
