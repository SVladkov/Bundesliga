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
    poll_all_matches,
    get_teams
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
    teams = get_teams(league_shortcut, league_season)

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
        update_team_points(match)


def get_unfinished_matches(league_shortcut, league_season):
    unfinished_matches = Match.objects.filter(is_finished=False)
    # and gameday is between last check and new gameday
    # yes, but update_match_points updates only matches that have result

    return unfinished_matches


def update_match_points(match_old_data, match_new_data):
    try:
        points_one = match_new_data['MatchResults'][1]['PointsTeam1']
        points_two = match_new_data['MatchResults'][1]['PointsTeam2']

        match_old_data.points_one = points_one
        match_old_data.points_two = points_two
        match_old_data.is_finished = True
        match_old_data.save(update_fields=['points_one', 'points_two', 'is_finished'])
    except Exception as e:
        pass


def update_team_points(match_new_data):
    try:
        team_one_id = match_new_data['Team1']['TeamId']
        team_two_id = match_new_data['Team2']['TeamId']

        points_one = match_new_data['MatchResults'][1]['PointsTeam1']
        points_two = match_new_data['MatchResults'][1]['PointsTeam2']

        team_one_wins_losses_season = Wins_Losses_Season.objects.get(team_id=team_one_id)
        team_two_wins_losses_season = Wins_Losses_Season.objects.get(team_id=team_two_id)

        if points_one > points_two:
            team_one_wins_losses_season.wins += 1
            team_two_wins_losses_season.loses += 1

            team_one_wins_losses_season.save(update_fields=['wins'])
            team_two_wins_losses_season.save(update_fields=['loses'])
        elif points_one < points_two:
            team_one_wins_losses_season.loses += 1
            team_two_wins_losses_season.wins += 1

            team_one_wins_losses_season.save(update_fields=['loses'])
            team_two_wins_losses_season.save(update_fields=['wins'])
    except Exception as e:
        print(e)
        pass



def update_points(league_shortcut, league_season):
    #maybe without last_checked_gameday
    # update just some of the gamedays
    all_matches_data = poll_all_matches(league_shortcut, league_season)
    all_matches_data_as_dict = {match['MatchID']: match for match in all_matches_data}

    unfinished_matches = get_unfinished_matches(league_shortcut, league_season)
    for match in unfinished_matches:
        match_new_data = all_matches_data_as_dict[int(match.match_id)]

        update_match_points(match, match_new_data)
        update_team_points(match_new_data)


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
            #get data about the season and update just points
            update_points(league_shortcut, current_season)
        else:
            #get data about the gameday and update just its points
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