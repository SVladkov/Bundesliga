from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_matches, name='index'),
    url(r'^bundesliga_app/allmatches/(?P<league_shortcut>[a-zA-Z0-9]+)/$', views.all_matches, name='allmatches'),
    url(r'^bundesliga_app/nextmatches/(?P<league_shortcut>[a-zA-Z0-9]+)/$', views.next_matches, name='nextmatches'),
    url(r'^bundesliga_app/winlossratio/(?P<league_shortcut>[a-zA-Z0-9]+)/$', views.win_loss_ratio, name='winlossratio'),
    url(r'^bundesliga_app/teams/$', views.teams, name='teams'),
    url(r'^bundesliga_app/teams/(?P<team_id>[0-9]+)/$', views.team, name='teams')
]