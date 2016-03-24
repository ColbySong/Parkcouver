# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0010_auto_20151120_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='imageURL',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
