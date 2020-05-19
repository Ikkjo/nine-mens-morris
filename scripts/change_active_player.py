from repos.player_repo import PlayerRepo
from modules.active_player import ActivePlayer


def change_active_player():
    active = ActivePlayer()
    players = PlayerRepo()

    if active.player == players.first:
        active.player = players.second
    else:
        active.player = players.first