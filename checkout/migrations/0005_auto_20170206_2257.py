# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 00:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20170206_2235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
    ]