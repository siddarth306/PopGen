# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 02:21
from __future__ import unicode_literals

import JobSchd.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0022_auto_20171218_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_to_sample',
            field=models.FileField(blank=True, help_text='geo_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='geo to sample'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_to_geo',
            field=models.FileField(blank=True, help_text='region_geo_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region to geo'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_to_sample',
            field=models.FileField(blank=True, help_text='region_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region to sample'),
        ),
    ]
