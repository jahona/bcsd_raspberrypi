# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('th', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='humu',
            new_name='humi',
        ),
    ]
