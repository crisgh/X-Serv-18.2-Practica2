# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acortarurl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url_Acortada',
            new_name='cortada',
        ),
        migrations.RenameField(
            model_name='url',
            old_name='urls',
            new_name='original',
        ),
    ]
