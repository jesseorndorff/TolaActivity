# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Fund Code')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='historicalsiteprofile',
            name='date_of_firstcontact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of First Contact'),
        ),
        migrations.AlterField(
            model_name='siteprofile',
            name='date_of_firstcontact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of First Contact'),
        ),
        migrations.AddField(
            model_name='program',
            name='fund_code',
            field=models.ManyToManyField(blank=True, to='activitydb.FundCode'),
        ),
    ]