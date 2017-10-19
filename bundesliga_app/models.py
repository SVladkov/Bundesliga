from django.db import models
from datetime import datetime


class Team(models.Model):
    name = models.CharField(max_length=60)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)

class Match(models.Model):
    match_id = models.CharField(max_length=5, primary_key=True)
    date = models.DateTimeField()
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    points_one = models.IntegerField(default=0)
    points_two = models.IntegerField(default=0)
    season = models.IntegerField()
    league = models.IntegerField()
    is_finished = models.BooleanField(default=False)

class Last_Checked(models.Model):
    season = models.IntegerField()
    gameday = models.IntegerField()
    date = models.DateTimeField()