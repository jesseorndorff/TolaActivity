# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-17 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0019_projectcomplete_stakeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='budget_check',
            field=models.BooleanField(default=False, verbose_name='Enable Approval Authority'),
        ),
    ]
