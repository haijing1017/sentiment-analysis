# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0007_auto_20160403_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsentiment',
            name='sentiment_api2',
            field=models.CharField(blank=True, choices=[(b'positive', b'Positive'), (b'negative', b'Negative'), (b'neutral', b'Neutral')], max_length=8, null=True),
        ),
    ]
