# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161105_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_number',
            field=models.CharField(default=1, max_length=4, unique=True),
            preserve_default=False,
        ),
    ]