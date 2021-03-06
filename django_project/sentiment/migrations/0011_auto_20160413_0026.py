# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-13 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0010_auto_20160411_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsentiment',
            name='sentiment_api1_en',
            field=models.CharField(blank=True, choices=[(b'positive', b'Positive'), (b'negative', b'Negative'), (b'neutral', b'Neutral')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='commentsentiment',
            name='sentiment_api2_en',
            field=models.CharField(blank=True, choices=[(b'positive', b'Positive'), (b'negative', b'Negative'), (b'neutral', b'Neutral')], max_length=8, null=True),
        ),
    ]
