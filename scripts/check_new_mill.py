from services.state_checker import StateChecker
from services.gameboard_service import GameboardService

def check_new_mill(last_moved_position):
    gameboard_state = GameboardService().gameboard.state
    return StateChecker.check_mill(gameboard_state, last_moved_position)