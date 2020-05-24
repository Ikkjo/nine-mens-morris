from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo


def display_active_player():
    green = "\u001b[32;1m"
    end = "\u001b[0m"
    players = PlayerRepo()
    active = ActivePlayer().player

    player2_type = players.player2.type
    player2 = {"human": "Player 2",
               "bor": "Bot"}

    if active == players.player1:
        player1 = green + "Player 1" + end
        player2 = player2[player2_type]
        print(f"{player1:<24}{player2:>24}", end="\n\n")
    elif active == players.player2:
        player1 = "Player 1"
        player2 = green + player2[player2_type] + end
        print(f"{player1:<24}{player2:>24}", end="\n\n")

