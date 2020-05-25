from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from scripts.next_move import next_move
from scripts.check_new_mill import check_new_mill


def initial_phase():
    mill = False
    active_player = ActivePlayer().player
    last_moved_position = next_move(active_player, "INIT")
    if check_new_mill(last_moved_position):
        mill = True

    return mill


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
