# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0011_park_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='imageURL',
            field=models.CharField(default=b'None', max_length=100),
        ),
    ]
