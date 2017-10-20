# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesliga_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='points_one',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='points_two',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
