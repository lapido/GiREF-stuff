# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giref', '0010_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='caption',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
