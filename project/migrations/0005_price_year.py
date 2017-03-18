# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-18 06:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='year',
            field=models.IntegerField(default=1, verbose_name='Year'),
            preserve_default=False,
        ),
    ]