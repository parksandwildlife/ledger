# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-07 06:35
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0018_auto_20181205_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalPark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_parks', to='commercialoperator.Park')),
                ('proposal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='commercialoperator.Proposal')),
            ],
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]
