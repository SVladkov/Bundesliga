from bundesliga_app.models import (
    Match,
    Wins_Losses_Season,
    Team
)
from django.db.models import Q

def create_wins_losses_season(team_id, league_shortcut, league_season):
    new_wins_losses_season = Wins_Losses_Season(
        team_id=team_id,
        wins=0,
        loses=0,
        season=league_season,
        league=league_shortcut
    )

    new_wins_losses_season.save()


def create_match(match, league_shortcut, league_season):
    if not match['MatchIsFinished']:
        points_one = None
        points_two = None
    else:
        points_one = match['MatchResults'][1]['PointsTeam1']
        points_two = match['MatchResults'][1]['PointsTeam2']

    new_match = Match(
        match_id=match['MatchID'],
        date=match['MatchDateTimeUTC'],
        team_one_id=match['Team1']['TeamId'],
        team_two_id=match['Team2']['TeamId'],
        points_one=points_one,
        points_two=points_two,
        season=league_season,
        league=league_shortcut,
        gameday = int(match['Group']['GroupName'].split('.')[0]),
        is_finished=match['MatchIsFinished']
    )
    new_match.save()


def get_unfinished_matches(league_shortcut, league_season):
    unfinished_matches = Match.objects.filter(league=league_shortcut, is_finished=False)

    return unfinished_matches


def get_all_matches(league_shortcut, league_season):
    matches = Match.objects.filter(league=league_shortcut, season=league_season).order_by('date')

    return matches


def get_matches_after_gameday(league_shortcut, league_season, current_gameday):
    matches = Match.objects.filter(league=league_shortcut, season=league_season, gameday__gt=current_gameday)

    return matches


def get_wins_losses(league_shortcut, league_season):
    win_loss_ratios = Wins_Losses_Season.objects.filter(league=league_shortcut, season=league_season)

    return win_loss_ratios


def get_teams_with_name(team_name):
    teams = Team.objects.filter(name__icontains=team_name)

    return teams


def get_wins_losses_for_team(team_id):
    wins_losses_for_team = Wins_Losses_Season.objects.get(team_id=team_id)

    return wins_losses_for_team


def get_past_matches_for_team(team_id):
    matches = Match.objects.filter(Q(team_one_id=team_id) | Q(team_two_id=team_id), is_finished=True)\
                           .select_related()\
                           .order_by('date')

    return matches


def get_next_matches_for_team(team_id):
    matches = Match.objects.filter(Q(team_one_id=team_id) | Q(team_two_id=team_id), is_finished=False)\
                           .select_related()\
                           .order_by('date')

    return matches
