# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0025_commentspam_spam_api1_with_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsentiment',
            name='is_mention',
            field=models.NullBooleanField(),
        ),
    ]
