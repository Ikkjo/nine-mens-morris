from repos.active_player import ActivePlayer
from scripts.next_move import next_move
from scripts.check_new_mill import check_new_mill


def initial_phase():
    mill = False
    active_player = ActivePlayer().player
    last_moved_position = next_move(active_player, "INIT")
    if check_new_mill(last_moved_position):
        mill = True

    return mill
