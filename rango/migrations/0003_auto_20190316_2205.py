# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20190316_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='postad',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]