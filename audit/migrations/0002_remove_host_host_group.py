# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-24 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='host_group',
        ),
    ]
