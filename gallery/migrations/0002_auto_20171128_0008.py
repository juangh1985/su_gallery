# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='cou',
            new_name='counter',
        ),
    ]
