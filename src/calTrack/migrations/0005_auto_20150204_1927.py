# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0004_auto_20150131_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fCalorie',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foods',
            name='fType',
            field=models.CharField(max_length=1, choices=[(b'l', b'Lunch'), (b'd', b'Dinner'), (b'b', b'Breakfast'), (b's', b'Snacks')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='amtOfExc',
            field=models.FloatField(default=0.0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'm', b'M'), (b'f', b'D')]),
            preserve_default=True,
        ),
    ]
