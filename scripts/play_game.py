from scripts.initial_phase import initial_phase
from scripts.move_phase import move_phase
from scripts.initialize_game import initialize_game


def play_game(mode: str):
    if initialize_game(mode) is False:
        return

    initial_phase()
    winner = move_phase()

    return winner











