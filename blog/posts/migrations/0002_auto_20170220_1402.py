# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.CharField(choices=[('oktatás', 'oktatás'), ('tudomány', 'tudomány'), ('politika', 'politika'), ('sport', 'sport')], default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
