from scripts.initial_phase import initial_phase, init_finishing_condition
from scripts.move_phase import move_phase, move_finishing_condition
from scripts.initialize_game import initialize_game
from scripts.play import play
from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo


def play_game(mode: str, debug=False):
    if initialize_game(mode, debug) is False:
        return
    ActivePlayer(PlayerRepo().player1)
    play(initial_phase, init_finishing_condition)
    winner = play(move_phase, move_finishing_condition)

    return winner
