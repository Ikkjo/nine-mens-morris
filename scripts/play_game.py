from scripts.initial_phase import initial_phase, init_finishing_condition
from scripts.move_phase import move_phase
from scripts.initialize_game import initialize_game
from scripts.play import play


def play_game(mode: str):
    if initialize_game(mode) is False:
        return

    play(initial_phase, init_finishing_condition)
    winner = play(move_phase)

    return winner
