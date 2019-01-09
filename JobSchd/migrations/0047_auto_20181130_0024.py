# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0046_auto_20180324_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='geo',
            field=models.CharField(max_length=50, verbose_name='Groupquaters Entity Name'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_groupquarter',
            field=models.CharField(help_text='e.g.  [gqtotals, gqtype]', max_length=50, verbose_name='Control Variable Geo Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_household',
            field=models.CharField(default='[hhtotals, hinc, hsize]', help_text='e.g.  [hhtotals, hinc, hsize]', max_length=50, verbose_name='Control Variable Geo Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_person',
            field=models.CharField(default='[pworker, ptotals]', help_text='e.g.  [pworker, ptotals] ', max_length=50, verbose_name='Control Variable Geo Person'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_groupquarter',
            field=models.CharField(help_text='e.g.  [gqrtotals]', max_length=50, verbose_name='Control Variable Region Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_household',
            field=models.CharField(default='[hhrtotals]', help_text='e.g.  [hhrtotals]', max_length=50, verbose_name='Control Variable Region Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_person',
            field=models.CharField(default='[rpsex, rpage, rpworker, prtotals]', help_text='e.g.  [rpsex, rpage, rpworker, prtotals]', max_length=50, verbose_name='Control Variable Region Person'),
        ),
    ]
