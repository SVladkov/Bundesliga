# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesliga_app', '0002_auto_20171019_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='gameday',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
