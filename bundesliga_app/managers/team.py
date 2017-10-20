from bundesliga_app.data.remote_data import (
    poll_current_season
)
from bundesliga_app.data.local_database import (
    get_wins_losses
)
from bundesliga_app.data.transformers import (
    transform_wins_losses
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
