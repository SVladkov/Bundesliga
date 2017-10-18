import urllib
import json

BASE_URL = 'https://www.openligadb.de/api/'


def get_url_response_as_json(url):
    response = urllib.request.urlopen(url).read()
    response_as_string = response.decode(encoding='UTF-8')
    response_as_json = json.loads(response_as_string)

    return response_as_json


def get_all_matches(league_shortcut, league_season):
    url = BASE_URL + 'getmatchdata/' + league_shortcut + '/' + league_season
    all_matches_data = get_url_response_as_json(url)

    return all_matches_data


def get_gameday(league_shortcut):
    url = BASE_URL + 'getcurrentgroup/' + league_shortcut
    response_as_json = get_url_response_as_json(url)
    group_name = response_as_json['GroupName']
    gameday = group_name.split('.')[0]

    return gameday


def get_current_season(league_shortcut):
    url = BASE_URL + 'getmatchdata/' + league_shortcut
    current_group = get_url_response_as_json(url)
    league_name = current_group[0]['LeagueName']
    current_season = league_name[-9:-5]

    return current_season


def get_next_matches(league_shortcut):
    gameday = get_gameday(league_shortcut)
    current_season = get_current_season(league_shortcut)

    all_matches_data = get_all_matches(league_shortcut, current_season)
    next_matches_data = [match for match in all_matches_data if int(match['Group']['GroupName'].split('.')[0]) > int(gameday)]

    return next_matches_data