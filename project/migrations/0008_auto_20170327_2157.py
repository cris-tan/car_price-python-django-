# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-27 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20170327_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='uk_avg_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='UK Average Price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='uk_high_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='UK High Price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='uk_low_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='UK Low Price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='usa_avg_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='USA Average Price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='usa_high_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='USA High Price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='usa_low_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='USA Low Price'),
        ),
    ]
