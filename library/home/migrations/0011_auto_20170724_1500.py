# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-24 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170724_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_entry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
