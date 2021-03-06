# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0013_auto_20150226_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fCalorie',
            field=models.PositiveIntegerField(default=1, max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
