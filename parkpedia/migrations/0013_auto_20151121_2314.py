# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0012_auto_20151121_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='imageURL',
            field=models.CharField(default=b'None', max_length=1000),
        ),
    ]
