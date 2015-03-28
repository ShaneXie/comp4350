# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0003_auto_20150131_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fType',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
    ]
