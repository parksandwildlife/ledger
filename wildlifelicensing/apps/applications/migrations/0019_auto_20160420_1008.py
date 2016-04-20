# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-20 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0018_auto_20160418_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='correctness_disclaimer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='further_information_disclaimer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='processing_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('new', 'New'), ('ready_for_action', 'Ready for Action'), ('awaiting_applicant_response', 'Awaiting Applicant Response'), ('awaiting_assessor_response', 'Awaiting Assessor Response'), ('awaiting_responses', 'Awaiting Responses'), ('ready_for_conditions', 'Ready for Conditions'), ('rejected', 'Rejected')], default='draft', max_length=30, verbose_name='Processing Status'),
        ),
    ]
