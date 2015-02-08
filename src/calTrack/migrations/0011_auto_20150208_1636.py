# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0010_auto_20150207_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(default=1, max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(default=0.0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(default=0.0, max_length=3),
            preserve_default=True,
        ),
    ]
