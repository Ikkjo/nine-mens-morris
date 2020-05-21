from interface.clear_screen import clear_screen
from interface.draw_gameboard import draw_gameboard
from modules.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from scripts.change_active_player import change_active_player
from scripts.next_move import next_move
from scripts.check_new_mill import check_new_mill


def initial_phase():
    while initial_is_not_finished():
        clear_screen()
        draw_gameboard()
        play_init()


def play_init():
    active_player = ActivePlayer().player
    next_move(active_player, "INIT")
    if check_new_mill():
        next_move(active_player, "MILL")
    change_active_player()


def initial_is_not_finished():
    player1 = PlayerRepo().player1
    player2 = PlayerRepo().player2

    if player1.has_unused_pieces or player2.has_unused_pieces:
        return True
    else:
        return False
