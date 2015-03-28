# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0007_auto_20150206_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fName',
            field=models.CharField(unique=True, max_length=25, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z]*$', b'Only alphanumeric characters are allowed.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')]),
            preserve_default=True,
        ),
    ]
