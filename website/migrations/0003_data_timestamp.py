# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170327_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2017, 3, 29)),
            preserve_default=False,
        ),
    ]