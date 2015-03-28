# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calTrack', '0009_auto_20150206_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.PositiveIntegerField(default=1)),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('amtOfExc', models.FloatField(default=0.0, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
