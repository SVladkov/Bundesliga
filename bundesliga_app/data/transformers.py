from bundesliga_app.utils import LEAGUE_SHORTCUTS_TO_FULL_NAMES

def transform_matches(matches):
    result = []

    for match in matches:
        team_one = match.team_one.name
        team_two = match.team_two.name

        transformed_match = {
            'date': match.date,
            'team_one_id': match.team_one_id,
            'team_two_id': match.team_two_id,
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
        team = wins_losses_team.team.name
        try:
            ratio = wins_losses_team.wins / wins_losses_team.loses
            ratio = "%.2f" % ratio
        except ZeroDivisionError:
            ratio = 'No losses'

        transformed_wins_losses = {
            'team_name': team,
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


def transform_team(wins_losses, past_matches, next_matches):
    try:
        ratio = wins_losses.wins / wins_losses.loses
        ratio = "%.2f" % ratio
    except ZeroDivisionError:
        ratio = 'No losses'

    transformed_team = {
        'name': wins_losses.team.name,
        'wins': wins_losses.wins,
        'losses': wins_losses.loses,
        'ratio': ratio,
        'league': LEAGUE_SHORTCUTS_TO_FULL_NAMES[wins_losses.league],
        'past_matches': transform_matches(past_matches),
        'next_matches': transform_matches(next_matches)
    }

    return transformed_team
