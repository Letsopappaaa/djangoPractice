# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170220_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='én', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 2, 22, 15, 51, 48, 745830, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_size',
            field=models.CharField(blank=True, choices=[('nagy', 'nagy'), ('kis', 'kis')], max_length=20, null=True),
        ),
    ]