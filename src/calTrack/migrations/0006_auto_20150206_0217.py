# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0005_auto_20150204_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fName',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='firstName',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='lastName',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
