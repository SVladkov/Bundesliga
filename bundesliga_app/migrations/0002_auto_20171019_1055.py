# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesliga_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='team_one_id',
            new_name='team_one',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='team_two_id',
            new_name='team_two',
        ),
    ]
