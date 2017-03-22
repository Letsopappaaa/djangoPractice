# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 10:34
from __future__ import unicode_literals

import accounts_and_comments.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('acc_created', models.DateTimeField(auto_now_add=True)),
                ('no_of_comments', models.IntegerField(blank=True, default=0)),
                ('last_sign_in', models.DateTimeField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to=accounts_and_comments.models.upload_location)),
                ('total_upvotes', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to=accounts_and_comments.models.upload_location_comment_img)),
                ('upvotes', models.IntegerField(default=0)),
                ('account_name', models.ForeignObject(from_fields=['upvotes'], on_delete=django.db.models.deletion.CASCADE, to='accounts_and_comments.account', to_fields=['total_upvotes'])),
            ],
        ),
    ]
