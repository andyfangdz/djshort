# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirect',
            name='destination',
            field=models.URLField(default='http://example.com', max_length=255),
            preserve_default=False,
        ),
    ]
