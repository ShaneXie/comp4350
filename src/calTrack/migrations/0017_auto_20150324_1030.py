# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0016_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='food',
            field=models.ForeignKey(to='calTrack.Foods'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
