from bundesliga_app.models import (
    Last_Checked,
    Match,
    Team,
    Wins_Losses_Season
)
from datetime import datetime
from dateutil.parser import parse
import pytz
from bundesliga_app.managers.remote_data import (
    get_current_gameday,
    get_current_season,
    get_last_change_date,
    poll_all_matches
)

from bundesliga_app.utils import get_url_response_as_json
BASE_URL = 'https://www.openligadb.de/api/'


def create_wins_losses_season(team_id, league_shortcut, league_season):
    new_wins_losses_season = Wins_Losses_Season(
        team_id=team_id,
        wins=0,
        loses=0,
        season=league_season,
        league=league_shortcut
    )

    new_wins_losses_season.save()


def update_teams(league_shortcut, league_season):
    url = BASE_URL + 'getavailableteams/' + league_shortcut + '/' + league_season
    teams = get_url_response_as_json(url)

    for team in teams:
        try:
            # This could happen at the beginning of new season
            Team.objects.get(team_id=team['TeamId'])
            create_wins_losses_season(team['TeamId'], league_shortcut, league_season)

        except Exception as e:
            # This could happen only if the team was never in the system
            new_team = Team(team_id=team['TeamId'], name=team['TeamName'])
            new_team.save()

            create_wins_losses_season(team['TeamId'], league_shortcut, league_season)


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
        is_finished=match['MatchIsFinished']
    )
    new_match.save()


def create_season(league_shortcut, league_season):
    update_teams(league_shortcut, league_season)

    all_matches_data = poll_all_matches(league_shortcut, league_season)
    for match in all_matches_data:
        create_match(match, league_shortcut, league_season)


def update_season(league_shortcut, league_season, last_checked_gameday):
    # update just some of the gamedays
    all_matches_data = poll_all_matches(league_shortcut, league_season)



def update_matches_if_needed(league_shortcut):
    current_season = get_current_season(league_shortcut)
    current_gameday = get_current_gameday(league_shortcut)

    last_checked = Last_Checked.objects.all()
    last_change_date = get_last_change_date(league_shortcut, current_season, current_gameday)

    if len(last_checked) == 0:
        # if application is never used before
        new_check = Last_Checked(season=current_season, gameday=current_gameday, date=last_change_date)
        new_check.save()

        create_season(league_shortcut, current_season)

    elif last_checked[0].date != parse(last_change_date).replace(tzinfo=pytz.utc):
        last_checked_season = last_checked[0].season
        last_checked_gameday = last_checked[0].gameday

        new_check = Last_Checked(season=current_season, gameday=current_gameday, date=last_change_date)
        new_check.save()

        if last_checked_season != current_season:
            #get data about the season and directly write it in the database
            create_season(league_shortcut, current_season)

        elif last_checked_gameday != current_gameday:
            #get data about the season and update just some gamedays
            update_season(league_shortcut, current_season, last_checked_gameday)
        else:
            #get data about the gameday and update just it
            pass

    all_matches_data = poll_all_matches(league_shortcut, current_season)
    print(all_matches_data[0]['MatchID'])


def get_all_matches(league_shortcut):
    current_season = get_current_season(league_shortcut)
    update_matches_if_needed(league_shortcut)

    url = BASE_URL + 'getmatchdata/' + league_shortcut + '/' + current_season
    all_matches_data = get_url_response_as_json(url)

    return all_matches_data


def gameday_of_a_match(match):
    return int(match['Group']['GroupName'].split('.')[0])


def get_next_matches(league_shortcut):
    gameday = get_current_gameday(league_shortcut)
    current_season = get_current_season(league_shortcut)

    all_matches_data = get_all_matches(league_shortcut)
    next_matches_data = [match for match in all_matches_data if gameday_of_a_match(match) > gameday]

    return next_matches_data