# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0005_auto_20160403_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsentiment',
            name='idcomment',
            field=models.OneToOneField(db_column='idcommento', on_delete=django.db.models.deletion.CASCADE, related_name='comment_sentiment', to='sentiment.Comment'),
        ),
    ]
