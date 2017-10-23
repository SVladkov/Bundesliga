import urllib
import json


LEAGUE_SHORTCUTS_TO_FULL_NAMES = {
    'bl1': 'Bundesliga 1',
    'bl2': 'Bundesliga 2',
    'bl3': 'Bundesliga 3'
}


def get_url_response_as_json(url):
    response = urllib.request.urlopen(url).read()
    response_as_string = response.decode(encoding='UTF-8')
    response_as_json = json.loads(response_as_string)

    return response_as_json
