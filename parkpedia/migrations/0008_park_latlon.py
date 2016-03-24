# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0007_auto_20151102_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='latLon',
            field=models.CharField(default=datetime.date(2015, 11, 19), max_length=40),
            preserve_default=False,
        ),
    ]
