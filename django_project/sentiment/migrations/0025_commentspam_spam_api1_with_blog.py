# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 17:38
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0024_auto_20160602_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentspam',
            name='spam_api1_with_blog',
            field=jsonfield.fields.JSONField(default=b'{"type": "", "is_spam": false}'),
        ),
    ]
