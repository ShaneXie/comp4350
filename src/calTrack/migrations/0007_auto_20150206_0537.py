# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0006_auto_20150206_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fName',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
    ]
