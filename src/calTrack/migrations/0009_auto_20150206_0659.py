# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0008_auto_20150206_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fName',
            field=models.CharField(unique=True, max_length=25, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only alphabets are allowed for the food name.')]),
            preserve_default=True,
        ),
    ]
