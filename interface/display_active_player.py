from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo


def display_active_player():
    green = "\u001b[32;1m"
    end = "\u001b[0m"
    players = PlayerRepo()
    active = ActivePlayer().player
    player1_type = players.player1.type
    player1 = {"human": "Player 1",
               "bot": "Bot"}

    player2_type = players.player2.type
    player2 = {"human": "Player 2",
               "bot": "Bot"}

    if active == players.player1:
        player1 = green + player1[player1_type] + end
        player2 = player2[player2_type]
        print(f"{player1:<24}{player2:>24}", end="\n\n")
    elif active == players.player2:
        player1 = player1[player1_type]
        player2 = green + player2[player2_type] + end
        print(f"{player1:<24}{player2:>24}", end="\n\n")

