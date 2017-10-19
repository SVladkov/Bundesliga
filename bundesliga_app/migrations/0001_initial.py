# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.CharField(serialize=False, max_length=5, primary_key=True)),
                ('date', models.DateTimeField()),
                ('points_one', models.IntegerField(default=0)),
                ('points_two', models.IntegerField(default=0)),
                ('season', models.IntegerField()),
                ('league', models.IntegerField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team_one_id',
            field=models.ForeignKey(related_name='team_one', to='bundesliga_app.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_two_id',
            field=models.ForeignKey(related_name='team_two', to='bundesliga_app.Team'),
        ),
    ]
