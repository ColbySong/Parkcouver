# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpedia', '0003_auto_20151026_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='streetName',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='streetNum',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='park',
            name='washroom',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
