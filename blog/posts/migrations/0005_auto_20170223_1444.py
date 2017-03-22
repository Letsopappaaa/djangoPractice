# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170222_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('acc_created', models.DateTimeField(auto_now_add=True)),
                ('no_of_posts', models.IntegerField(default=0)),
                ('last_sign_in', models.DateTimeField()),
                ('facebook_link', models.URLField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_style',
            field=models.CharField(choices=[('kép_alatt_fekete', 'kép_alatt_fekete'), ('kép_alatt_sárga', 'kép_alattsárga'), ('kép_alatt_sima', 'kép_alatt_sima'), ('kép_felett_sárga', 'kép_felett_sárga'), ('kép_felett_fekete', 'kép_felett_fekete'), ('képen_alul_sárga', 'képen_alul_sárga'), ('képen_felül_fekete', 'képen_felül_fekete')], max_length=100),
        ),
    ]
