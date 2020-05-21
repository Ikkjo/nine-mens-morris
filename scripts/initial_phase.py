from modules.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from scripts.next_move import next_move
from scripts.check_new_mill import check_new_mill


def initial_phase():
    active_player = ActivePlayer().player
    next_move(active_player, "INIT")
    if check_new_mill():
        next_move(active_player, "MILL")


def init_finishing_condition():
    return do_players_have_unused_pieces()


def do_players_have_unused_pieces():
    player1 = PlayerRepo().player1
    player2 = PlayerRepo().player2

    if player1.has_unused_pieces or player2.has_unused_pieces:
        return True
    else:
        return False
