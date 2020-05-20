from modules.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from scripts.change_active_player import change_active_player
from scripts.next_move import next_move
from services.state_checker import StateChecker


def initial_phase():
    while initial_is_not_finished():
        play_init()


def play_init():
    active_player = ActivePlayer().player
    next_move(active_player, "INIT")
    if new_mill():
        next_move(active_player, "MILL")
    change_active_player()


def initial_is_not_finished():
    player1 = PlayerRepo().player1
    player2 = PlayerRepo().player2

    if player1.has_unused_pieces or player2.has_unused_pieces:
        return True
    else:
        return False


def new_mill():
    return StateChecker.check_mills()
