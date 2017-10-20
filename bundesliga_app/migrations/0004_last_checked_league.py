# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesliga_app', '0003_match_gameday'),
    ]

    operations = [
        migrations.AddField(
            model_name='last_checked',
            name='league',
            field=models.CharField(max_length=3, default='bl1'),
            preserve_default=False,
        ),
    ]
