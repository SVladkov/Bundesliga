from bundesliga_app.models import (
    Team
)

def transform_matches(matches):
    result = []

    for match in matches:
        team_one = Team.objects.get(team_id=match.team_one_id).name
        team_two = Team.objects.get(team_id=match.team_two_id).name

        transformed_match = {
            'date': match.date,
            'team_one': team_one,
            'team_two': team_two,
            'points_one': match.points_one,
            'points_two': match.points_two
        }

        result.append(transformed_match)

    return result


def transform_wins_losses(wins_losses):
    result = []

    for wins_losses_team in wins_losses:
        team = Team.objects.get(team_id=wins_losses_team.team_id)
        try:
            ratio = wins_losses_team.wins / wins_losses_team.loses
            ratio = "%.2f" % ratio
        except ZeroDivisionError:
            ratio = 'No losses'

        transformed_wins_losses = {
            'team_name': team.name,
            'wins': wins_losses_team.wins,
            'losses': wins_losses_team.loses,
            'ratio': ratio
        }

        result.append(transformed_wins_losses)

    return result


def transform_teams(teams):
    result = []

    for team in teams:
        transformed_team = {
            'id': team.team_id,
            'name': team.name
        }

        result.append(transformed_team)
        print(transformed_team)

    return result


def transform_team(wins_losses, matches):
    try:
        ratio = wins_losses.wins / wins_losses.loses
        ratio = "%.2f" % ratio
    except ZeroDivisionError:
        ratio = 'No losses'

    league_shortcuts = {
        'bl1': 'Bundesliga 1',
        'bl2': 'Bundesliga 2',
        'bl3': 'Bundesliga 3'
    }

    transformed_team = {
        'name': wins_losses.team.name,
        'wins': wins_losses.wins,
        'losses': wins_losses.loses,
        'ratio': ratio,
        'league': league_shortcuts[wins_losses.league],
        'matches': transform_matches(matches)
    }

    return transformed_team
