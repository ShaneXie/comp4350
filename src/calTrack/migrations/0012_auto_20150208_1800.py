# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0011_auto_20150208_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='amtOfExc',
            field=models.PositiveIntegerField(default=0.0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(default=1.0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(default=1.0, max_length=3),
            preserve_default=True,
        ),
    ]
