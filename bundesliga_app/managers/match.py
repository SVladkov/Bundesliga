import urllib
import json
from bundesliga_app.models import (
    Last_Checked,
    Match,
    Team
)
from datetime import datetime
from dateutil.parser import parse
import pytz


BASE_URL = 'https://www.openligadb.de/api/'


def get_current_gameday(league_shortcut):
    url = BASE_URL + 'getcurrentgroup/' + league_shortcut
    response_as_json = get_url_response_as_json(url)
    group_name = response_as_json['GroupName']
    gameday = int(group_name.split('.')[0])

    return gameday


def get_current_season(league_shortcut):
    url = BASE_URL + 'getmatchdata/' + league_shortcut
    current_group = get_url_response_as_json(url)
    league_name = current_group[0]['LeagueName']
    current_season = league_name[-9:-5]

    return current_season


def get_url_response_as_json(url):
    response = urllib.request.urlopen(url).read()
    response_as_string = response.decode(encoding='UTF-8')
    response_as_json = json.loads(response_as_string)

    return response_as_json


def get_last_change_date(league_shortcut, league_season, league_gameday):
    url = BASE_URL + 'getlastchangedate/' + league_shortcut + '/' + league_season + '/' + str(league_gameday)
    last_change_date = get_url_response_as_json(url)

    return last_change_date


def poll_all_matches(league_shortcut, league_season):
    url = BASE_URL + 'getmatchdata/' + league_shortcut + '/' + league_season
    all_matches_data = get_url_response_as_json(url)

    return all_matches_data


def update_matches_if_needed(league_shortcut):
    current_season = get_current_season(league_shortcut)
    current_gameday = get_current_gameday(league_shortcut)

    last_checked = Last_Checked.objects.all()
    last_change_date = get_last_change_date(league_shortcut, current_season, current_gameday)

    if len(last_checked) == 0 or last_checked[0].date != parse(last_change_date).replace(tzinfo=pytz.utc):
        new_check = Last_Checked(season=current_season, gameday=current_gameday, date=last_change_date)
        new_check.save()

        all_matches_data = poll_all_matches(league_shortcut, current_season)

        print(all_matches_data)


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