# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from ledger.payments.utils import update_payments

def updateInvoices(apps, schema_editor):
    Invoice = apps.get_model('payments','Invoice')
    try:
        for i in Invoice.objects.all():
            update_payments(i.reference)
    except:
        raise

def reverse_func(apps, schema_editor):
    DEFAULT_PAYMENT = {
        'bpay': {},
        'cash': {},
        'card': {}
    }
    Order = apps.get_model('order','Order')
    for o in Order.objects.all():
        for l in o.lines.all():
            l.payment_details = DEFAULT_PAYMENT
            l.refund_details = DEFAULT_PAYMENT
            l.save()


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20170411_1203'),
    ]

    operations = [
        # FIXME: there's absolutely no way to make update_payments work in a
        # migration, when the models in question are using a past version of the schema.
        # best case is to run it afterwards?
        #migrations.RunPython(updateInvoices, reverse_func)
    ]
