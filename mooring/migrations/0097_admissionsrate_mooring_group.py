# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-08 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0096_auto_20190104_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionsrate',
            name='mooring_group',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mooring.MooringAreaGroup'),
            preserve_default=False,
        ),
    ]