# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesliga_app', '0002_auto_20171019_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_Checked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('season', models.IntegerField()),
                ('gameday', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
