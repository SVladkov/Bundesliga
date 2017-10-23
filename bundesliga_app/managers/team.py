from bundesliga_app.data.remote_data import (
    poll_current_season
)
from bundesliga_app.data.local_database import (
    get_wins_losses,
    get_teams_with_name,
    get_wins_losses_for_team,
    get_next_matches_for_team,
    get_past_matches_for_team
)
from bundesliga_app.data.transformers import (
    transform_wins_losses,
    transform_teams,
    transform_team
)
from bundesliga_app.managers.match import (
    update_matches_if_needed
)


def win_loss_ratios(league_shortcut):
    update_matches_if_needed(league_shortcut)

    current_season = poll_current_season(league_shortcut)
    wins_losses = get_wins_losses(league_shortcut, current_season)

    transformed_wins_losses = transform_wins_losses(wins_losses)

    return transformed_wins_losses


def search_teams(team_name):
    teams = get_teams_with_name(team_name)

    transformed_teams = transform_teams(teams)

    return transformed_teams


def search_team(team_id):
    wins_losses = get_wins_losses_for_team(team_id)
    past_matches = get_past_matches_for_team(team_id)
    next_matches = get_next_matches_for_team(team_id)

    transformed_team = transform_team(wins_losses, past_matches, next_matches)

    return transformed_team
