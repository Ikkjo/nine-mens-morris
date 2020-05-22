from services.state_checker import StateChecker
from services.gameboard_service import GameboardService

def check_new_mill():
    gameboard_state = GameboardService().gameboard.state
    return StateChecker.check_mills(gameboard_state)