# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-30 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20190329_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]
