# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-24 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170724_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_entry',
            name='date_of_issue',
        ),
        migrations.AddField(
            model_name='book_entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 24, 14, 59, 24, 136211)),
        ),
    ]