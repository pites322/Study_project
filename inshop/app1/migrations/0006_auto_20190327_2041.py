# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20190324_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='None', upload_to='media/'),
        ),
    ]