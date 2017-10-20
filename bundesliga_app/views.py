from django.http import HttpResponse
from django.shortcuts import render
from bundesliga_app.managers.match import (
    get_all_matches,
    get_next_matches
)
from bundesliga_app.managers.team import win_loss_ratios

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

    return render(request, 'bundesliga_app/index.html', context)

def win_loss_ratio(request, league_shortcut):
    win_loss_ratio_data = win_loss_ratios(league_shortcut)

    print(win_loss_ratio_data)

    context = {
        'win_loss_ratio_data': win_loss_ratio_data
    }

    return render(request, 'bundesliga_app/win_loss_ratio.html', context)
