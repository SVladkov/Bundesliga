from django.db import models
from datetime import datetime


class Team(models.Model):
    team_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=60)


class Wins_Losses_Season(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    season = models.IntegerField()
    league = models.CharField(max_length=3)


class Match(models.Model):
    match_id = models.CharField(max_length=5, primary_key=True)
    date = models.DateTimeField()
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    points_one = models.IntegerField(default=0, null=True)
    points_two = models.IntegerField(default=0, null=True)
    season = models.IntegerField()
    league = models.CharField(max_length=3)
    gameday = models.IntegerField()
    is_finished = models.BooleanField(default=False)


class Last_Checked(models.Model):
    league = models.CharField(max_length=3)
    season = models.IntegerField()
    gameday = models.IntegerField()
    date = models.DateTimeField()