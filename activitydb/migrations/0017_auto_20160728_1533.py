# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-28 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0016_auto_20160727_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteprofile',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.Office'),
        ),
    ]
