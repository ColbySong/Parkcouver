# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='facilities',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
