# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0011_park_specialfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='imageURL',
            field=models.CharField(default=b'None', max_length=1000),
            preserve_default=True,
        ),
    ]
