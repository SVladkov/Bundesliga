# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Last_Checked',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('season', models.IntegerField()),
                ('gameday', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('points_one', models.IntegerField(default=0)),
                ('points_two', models.IntegerField(default=0)),
                ('season', models.IntegerField()),
                ('league', models.CharField(max_length=3)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Wins_Losses_Season',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('season', models.IntegerField()),
                ('league', models.CharField(max_length=3)),
                ('team', models.ForeignKey(to='bundesliga_app.Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team_one',
            field=models.ForeignKey(to='bundesliga_app.Team', related_name='team_one'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_two',
            field=models.ForeignKey(to='bundesliga_app.Team', related_name='team_two'),
        ),
    ]
