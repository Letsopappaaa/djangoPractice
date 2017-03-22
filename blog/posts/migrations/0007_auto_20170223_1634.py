# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170223_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='author',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_sign_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='no_of_posts',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
