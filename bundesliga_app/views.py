from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib

def index(request):
    return HttpResponse("Hello world")

def all_matches(request, league_shortcut, league_season):
    base_url = 'https://www.openligadb.de/api/getmatchdata/'
    url = base_url + league_shortcut + "/" + league_season
    response = urllib.request.urlopen(url).read()
    all_matches_data_as_string = response.decode(encoding='UTF-8')
    all_matches_data = json.loads(all_matches_data_as_string)

    context = {
        'all_matches_data': all_matches_data
    }

    return render(request, 'bundesliga_app/index.html', context)