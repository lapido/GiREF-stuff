# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giref', '0008_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='website',
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]