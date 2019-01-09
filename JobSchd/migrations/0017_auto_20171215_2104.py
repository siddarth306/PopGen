# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0016_auto_20171215_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfinal',
            name='SmplSpatialUn',
            field=models.CharField(default='Sample', help_text='PUMA', max_length=50, verbose_name='Sample Spatial Unit'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='apf',
            field=models.IntegerField(default=1, verbose_name='Archive Performance Frequency'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='arc',
            field=models.BooleanField(default=True, verbose_name='Apply Region Controls'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='collate_across_geos',
            field=models.BooleanField(default=False, verbose_name='Collate Across Geos'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='desc',
            field=models.CharField(default='Brief description', help_text='Connecticut TAZ Scenario', max_length=50, verbose_name='Scenario Description'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='draws_iterations',
            field=models.IntegerField(default=1, verbose_name='Iterations'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='entities',
            field=models.CharField(default='[household, groupquarter, person]', help_text='[household, groupquarter, person]', max_length=50, verbose_name='Entities'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='entity',
            field=models.CharField(default='person', help_text='household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='export',
            field=models.BooleanField(default=True, verbose_name='Export'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filename',
            field=models.CharField(default='hhsize_income.csv', help_text='hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filetype',
            field=models.CharField(default='csv', help_text='csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_all_ids',
            field=models.BooleanField(default=True, verbose_name='Geo All Ids'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_groupquarter',
            field=models.CharField(default='', help_text='eg. [gqtotals, gqtype]', max_length=50, verbose_name='Geo Groupquarter'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_household',
            field=models.CharField(default='', help_text='eg. [hhtotals, hinc, hsize] ', max_length=50, verbose_name='Geo Household'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_ids',
            field=models.CharField(default=['[1,2,3'], help_text='[1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=50, verbose_name='Geo Ids'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_person',
            field=models.CharField(default='', help_text='eg. [pworker, ptotals] ', max_length=50, verbose_name='Geo Person'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='housing_entities',
            field=models.CharField(default='[household, groupquarter]', help_text='[household, groupquarter]', max_length=50, verbose_name='Housing Entities'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='inner_iterations',
            field=models.IntegerField(default=1, verbose_name='Inner Iterations'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='ipf_tolerance',
            field=models.DecimalField(decimal_places=10, default=0.0001, max_digits=20, verbose_name='Tolerance'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='iterations',
            field=models.IntegerField(default=1, max_length=10, verbose_name='Iterations'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='multiway_variables',
            field=models.CharField(default='[hsize, hinc]', help_text='[hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='outer_iterations',
            field=models.IntegerField(default=1000, verbose_name='Outer Iterations'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='performance',
            field=models.CharField(default='[ipf, reweighting, drawing]', help_text='[ipf, reweighting, drawing]', max_length=50, verbose_name='Performance'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='person_entities',
            field=models.CharField(default='[person]', help_text='[person]', max_length=50, verbose_name='Person Entities'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='procedure',
            field=models.CharField(choices=[('IPU', 'IPU'), ('Entropy', 'Entropy')], default='IPU', max_length=50, verbose_name='Procedure'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='pvalue_tolerance',
            field=models.DecimalField(decimal_places=10, default=0.9999, max_digits=20, verbose_name='Pvalue Tolerance'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='rapf',
            field=models.IntegerField(default=1, verbose_name='Archive Performance Frequency'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_all_ids',
            field=models.BooleanField(default=True, verbose_name='Region All Ids'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_groupquarter',
            field=models.CharField(default='', help_text='eg. [gqrtotals]', max_length=50, verbose_name='Region Groupquarter'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_household',
            field=models.CharField(default='', help_text='eg. [hhrtotals]', max_length=50, verbose_name='Region Household'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_ids',
            field=models.CharField(default=['[1,2,3'], help_text='[1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=50, verbose_name='Region Ids'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_person',
            field=models.CharField(default='', help_text='eg. [rpsex, rpage, rpworker, prtotals]', max_length=50, verbose_name='Region Person'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='rew_tolerance',
            field=models.DecimalField(decimal_places=10, default=0.0001, max_digits=20, verbose_name='Tolerance'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='rp',
            field=models.CharField(choices=[('bucket', 'bucket')], default='bucket', max_length=50, verbose_name='Rounding Procedure'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='seed',
            field=models.IntegerField(default=0, verbose_name='Seed'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='zmc',
            field=models.DecimalField(decimal_places=10, default=1e-05, max_digits=20, verbose_name='Zero Marginal Correction'),
        ),
    ]
