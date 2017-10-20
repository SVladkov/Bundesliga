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
