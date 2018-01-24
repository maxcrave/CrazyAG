# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-24 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0003_auto_20180124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostuser',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='hostuser',
            unique_together=set([('auth_type', 'username', 'password')]),
        ),
    ]
