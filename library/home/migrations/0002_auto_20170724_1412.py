# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-24 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='book',
            new_name='book_entry',
        ),
    ]
