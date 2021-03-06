# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 08:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_status', models.CharField(choices=[('draft', 'Draft'), ('under_review', 'Under Review'), ('id_required', 'Identification Required'), ('returns_required', 'Returns Completion Required'), ('amendment_required', 'Amendment Required'), ('id_and_amendment_required', 'Identification/Amendments Required'), ('id_and_returns_required', 'Identification/Returns Required'), ('returns_and_amendment_required', 'Returns/Amendments Required'), ('id_and_returns_and_amendment_required', 'Identification/Returns/Amendments Required'), ('approved', 'Approved'), ('declined', 'Declined')], default='draft', max_length=40, verbose_name='Customer Status')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('correctness_disclaimer', models.BooleanField(default=False)),
                ('further_information_disclaimer', models.BooleanField(default=False)),
                ('lodgement_number', models.CharField(blank=True, default='', max_length=9)),
                ('lodgement_sequence', models.IntegerField(blank=True, default=0)),
                ('lodgement_date', models.DateField(blank=True, null=True)),
                ('processing_status', models.CharField(choices=[('draft', 'Draft'), ('new', 'New'), ('renewal', 'Renewal'), ('ready_for_action', 'Ready for Action'), ('awaiting_applicant_response', 'Awaiting Applicant Response'), ('awaiting_assessor_response', 'Awaiting Assessor Response'), ('awaiting_responses', 'Awaiting Responses'), ('ready_for_conditions', 'Ready for Conditions'), ('ready_to_issue', 'Ready to Issue'), ('issued', 'Issued'), ('declined', 'Declined')], default='draft', max_length=30, verbose_name='Processing Status')),
                ('id_check_status', models.CharField(choices=[('not_checked', 'Not Checked'), ('awaiting_update', 'Awaiting Update'), ('updated', 'Updated'), ('accepted', 'Accepted')], default='not_checked', max_length=30, verbose_name='Identification Check Status')),
                ('returns_check_status', models.CharField(choices=[('not_checked', 'Not Checked'), ('awaiting_returns', 'Awaiting Returns'), ('completed', 'Completed'), ('accepted', 'Accepted')], default='not_checked', max_length=30, verbose_name='Return Check Status')),
                ('character_check_status', models.CharField(choices=[('not_checked', 'Not Checked'), ('accepted', 'Accepted')], default='not_checked', max_length=30, verbose_name='Character Check Status')),
                ('review_status', models.CharField(choices=[('not_reviewed', 'Not Reviewed'), ('awaiting_amendments', 'Awaiting Amendments'), ('amended', 'Amended'), ('accepted', 'Accepted')], default='not_reviewed', max_length=30, verbose_name='Review Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('acceptance_status', models.CharField(choices=[('not_specified', 'Not Specified'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='not_specified', max_length=20, verbose_name='Acceptance Status')),
            ],
        ),
        migrations.CreateModel(
            name='AmendmentRequest',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('amended', 'Amended')], default='requested', max_length=30, verbose_name='Status')),
                ('reason', models.CharField(choices=[('insufficient_detail', 'The information provided was insufficient'), ('missing_information', 'There was missing information'), ('other', 'Other')], default='insufficient_detail', max_length=30, verbose_name='Reason')),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('status', models.CharField(choices=[('awaiting_assessment', 'Awaiting Assessment'), ('assessed', 'Assessed')], default='awaiting_assessment', max_length=20, verbose_name='Status')),
                ('comment', models.TextField(blank=True)),
                ('purpose', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
        migrations.CreateModel(
            name='CustomLogEntry',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('subject', models.CharField(blank=True, max_length=200, verbose_name='Subject / Description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
        migrations.CreateModel(
            name='EmailLogEntry',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('subject', models.CharField(blank=True, max_length=500)),
                ('to', models.CharField(blank=True, max_length=500, verbose_name='To')),
                ('from_email', models.CharField(blank=True, max_length=200, verbose_name='From')),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
        migrations.CreateModel(
            name='IDRequest',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('reason', models.CharField(choices=[('missing', 'There is currently no Photographic Identification uploaded'), ('expired', 'The current identification has expired'), ('not_recognised', 'The current identification is not recognised by the Department of Parks and Wildlife'), ('illegible', 'The current identification image is of poor quality and cannot be made out.'), ('other', 'Other')], default='missing', max_length=30, verbose_name='Reason')),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
        migrations.CreateModel(
            name='ReturnsRequest',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wl_applications.ApplicationLogEntry')),
                ('reason', models.CharField(choices=[('outstanding', 'There are currently outstanding returns for the previous licence'), ('other', 'Other')], default='outstanding', max_length=30, verbose_name='Reason')),
            ],
            options={
                'abstract': False,
            },
            bases=('wl_applications.applicationlogentry',),
        ),
    ]
