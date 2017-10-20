import urllib
import json


def get_url_response_as_json(url):
    response = urllib.request.urlopen(url).read()
    response_as_string = response.decode(encoding='UTF-8')
    response_as_json = json.loads(response_as_string)

    return response_as_json