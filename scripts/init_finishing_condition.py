from repos.player_repo import PlayerRepo


def init_finishing_condition():
    return do_players_have_unused_pieces()


def do_players_have_unused_pieces():
    p_repo = PlayerRepo()
    player1 = p_repo.player1
    player2 = p_repo.player2

    if player1.has_unused_pieces or player2.has_unused_pieces:
        return True
    else:
        return False