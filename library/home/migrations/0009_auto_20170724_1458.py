# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-24 14:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170724_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_entry',
            name='date_of_issue',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 24, 14, 58, 53, 558372)),
        ),
    ]
