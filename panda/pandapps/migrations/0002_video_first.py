# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='first',
            field=models.BooleanField(default=True),
        ),
    ]
