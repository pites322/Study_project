# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-20 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20190320_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='app1/static/images/'),
        ),
    ]
