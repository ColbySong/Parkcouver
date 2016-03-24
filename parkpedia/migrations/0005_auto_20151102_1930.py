# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0004_auto_20151027_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='facilities',
            field=models.CharField(default=b'None', max_length=128),
        ),
    ]
