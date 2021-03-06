# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-29 05:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20170920_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='deduction_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
        migrations.AlterField(
            model_name='line',
            name='payment_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
        migrations.AlterField(
            model_name='line',
            name='refund_details',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, default={'bpay': {}, 'card': {}, 'cash': {}}),
        ),
    ]
