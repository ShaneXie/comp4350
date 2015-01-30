# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calTrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('amtOfExc', models.FloatField(default=0.0)),
                ('gneder', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
