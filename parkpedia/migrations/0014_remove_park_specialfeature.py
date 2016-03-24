# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0013_auto_20151123_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='specialFeature',
        ),
    ]
