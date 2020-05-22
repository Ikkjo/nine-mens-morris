from services.gameboard_service import GameboardService


class StateChecker(object):

    @staticmethod
    def check_mills(board_state):
        pass

    @staticmethod
    def is_position_occupied(row, column):
        board_state = GameboardService().get_gameboard_state()
        return board_state[row][column].piece != 'o'
