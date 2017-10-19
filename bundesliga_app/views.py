from django.http import HttpResponse
from django.shortcuts import render
from bundesliga_app.managers.match import (
    get_all_matches,
    get_next_matches
)
from bundesliga_app.models import Team
from datetime import datetime

def index(request):
    return HttpResponse("Hello world")

def all_matches(request, league_shortcut):
    all_matches_data = get_all_matches(league_shortcut)

    context = {
        'matches_data': all_matches_data
    }

    return render(request, 'bundesliga_app/index.html', context)

def next_matches(request, league_shortcut):
    next_matches_data = get_next_matches(league_shortcut)

    context = {
        'matches_data': next_matches_data
    }

    a = Team(name='Team', wins=1, loses=3)
    a.save()

    return render(request, 'bundesliga_app/index.html', context)