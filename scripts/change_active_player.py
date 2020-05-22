from repos.player_repo import PlayerRepo
from repos.active_player import ActivePlayer


def change_active_player():
    active = ActivePlayer()
    players = PlayerRepo()

    if active.player == players.player1:
        active.player = players.player2
    else:
        active.player = players.player1