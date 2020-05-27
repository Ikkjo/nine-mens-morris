from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from scripts.next_move import next_move
from scripts.check_new_mill import check_new_mill


def move_phase():
    mill = False
    active_player = ActivePlayer().player
    last_moved_position = next_move(active_player, "INIT")
    if check_new_mill(last_moved_position):
        mill = True

    return mill


def move_finishing_condition():
    players = PlayerRepo().players
    phase_over = False
    for player in players:
        if losing_condition(player):
            phase_over = True

    return phase_over


def losing_condition(player):
    losing_number_of_pieces = 2
    return player.pieces_left == losing_number_of_pieces
