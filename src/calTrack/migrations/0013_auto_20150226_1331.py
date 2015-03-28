# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0012_auto_20150208_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fType',
            field=models.CharField(max_length=10, choices=[(b'Lunch', b'Lunch'), (b'Dinner', b'Dinner'), (b'Breakfast', b'Breakfast'), (b'Snacks', b'Snacks')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
    ]
