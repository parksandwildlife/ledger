# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0052_auto_20170324_1313'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OracleInterface',
        ),
    ]