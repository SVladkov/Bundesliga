from django.http import HttpResponse
from django.shortcuts import render
from bundesliga_app.managers.match import (
    get_all_matches,
    get_next_matches
)
from bundesliga_app.managers.team import (
    win_loss_ratios,
    search_teams,
    search_team
)
from bundesliga_app.utils import LEAGUE_SHORTCUTS_TO_FULL_NAMES


def index(request):
    return HttpResponse("Hello world")


def all_matches(request, league_shortcut='bl1'):
    all_matches_data = get_all_matches(league_shortcut)

    context = {
        'matches_data': all_matches_data,
        'league': LEAGUE_SHORTCUTS_TO_FULL_NAMES[league_shortcut]
    }

    return render(request, 'bundesliga_app/index.html', context)


def next_matches(request, league_shortcut):
    next_matches_data = get_next_matches(league_shortcut)

    context = {
        'matches_data': next_matches_data,
        'league': LEAGUE_SHORTCUTS_TO_FULL_NAMES[league_shortcut]
    }

    return render(request, 'bundesliga_app/index.html', context)


def win_loss_ratio(request, league_shortcut):
    win_loss_ratio_data = win_loss_ratios(league_shortcut)

    context = {
        'win_loss_ratio_data': win_loss_ratio_data,
        'league': LEAGUE_SHORTCUTS_TO_FULL_NAMES[league_shortcut]
    }

    return render(request, 'bundesliga_app/win_loss_ratio.html', context)


def teams(request):
    search_name = request.GET.get('name')
    teams = search_teams(search_name)

    context = {
        'search_name': search_name,
        'teams': teams
    }

    return render(request, 'bundesliga_app/teams.html', context)


def team(request, team_id):
    team = search_team(team_id)

    context = {
        'team': team
    }

    return render(request, 'bundesliga_app/team.html', context)
