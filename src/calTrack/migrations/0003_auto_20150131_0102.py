# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0002_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='gneder',
            new_name='gender',
        ),
    ]
