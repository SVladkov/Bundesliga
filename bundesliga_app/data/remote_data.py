from bundesliga_app.utils import get_url_response_as_json

BASE_URL = 'https://www.openligadb.de/api/'

def poll_current_gameday(league_shortcut):
    url = BASE_URL + 'getcurrentgroup/' + league_shortcut
    response_as_json = get_url_response_as_json(url)
    group_name = response_as_json['GroupName']
    gameday = int(group_name.split('.')[0])

    return gameday


def poll_current_season(league_shortcut):
    url = BASE_URL + 'getmatchdata/' + league_shortcut
    current_group = get_url_response_as_json(url)
    league_name = current_group[0]['LeagueName']
    current_season = league_name[-9:-5]

    return current_season


def poll_last_change_date(league_shortcut, league_season, league_gameday):
    url = BASE_URL + 'getlastchangedate/' + league_shortcut + '/' + league_season + '/' + str(league_gameday)
    last_change_date = get_url_response_as_json(url)

    return last_change_date


def poll_all_matches(league_shortcut, league_season):
    url = BASE_URL + 'getmatchdata/' + league_shortcut + '/' + league_season
    all_matches_data = get_url_response_as_json(url)

    return all_matches_data


def poll_teams(league_shortcut, league_season):
    url = BASE_URL + 'getavailableteams/' + league_shortcut + '/' + league_season
    teams = get_url_response_as_json(url)

    return teams