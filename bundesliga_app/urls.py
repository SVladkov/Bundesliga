from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allmatches/(?P<league_shortcut>[a-zA-Z0-9]+)/(?P<league_season>[0-9]+)/$', views.all_matches, name='allmatches'),
    url(r'^nextmatches/(?P<league_shortcut>[a-zA-Z0-9]+)/$', views.next_matches, name='nextmatches')
]