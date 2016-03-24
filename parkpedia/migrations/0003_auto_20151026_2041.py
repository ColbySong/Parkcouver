# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0002_park_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
