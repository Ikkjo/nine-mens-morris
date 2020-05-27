from repos.player_repo import PlayerRepo


def display_winner(winner):
    out = who_won(winner)
    print(out)
    input("Press any key to continue...")


def who_won(winner):
    players = PlayerRepo()
    out = "{0} wins!"

    if winner == players.player1:
        out.format("Player 1")

    elif winner.type == "bot":
        out.format("Bot")
    else:
        out.format("Player 2")

    return out
