# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-29 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20190327_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='connection_range',
            field=models.CharField(blank=True, default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='wire_lenght',
            field=models.DecimalField(blank=True, decimal_places=1, default='0', max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='work_time',
            field=models.CharField(blank=True, default='0', max_length=60),
        ),
    ]