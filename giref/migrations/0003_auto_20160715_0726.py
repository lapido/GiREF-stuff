# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giref', '0002_girefprojects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GirefProjects',
            new_name='GirefProject',
        ),
    ]
