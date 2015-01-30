# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fName', models.CharField(max_length=50)),
                ('fCalorie', models.IntegerField(default=0)),
                ('fType', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
