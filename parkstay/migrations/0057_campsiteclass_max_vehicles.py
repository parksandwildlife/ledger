# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0056_auto_20170404_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='campsiteclass',
            name='max_vehicles',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
