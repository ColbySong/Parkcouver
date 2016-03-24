# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0012_park_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='specialFeature',
            field=models.CharField(max_length=128),
        ),
    ]
