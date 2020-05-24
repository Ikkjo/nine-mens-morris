from services.gameboard_service import GameboardService


class StateChecker(object):

    @staticmethod
    def check_mills(board_state, last_moved_position):
        lmp_row = last_moved_position[0]
        lmp_column = last_moved_position[1]
        position = board_state[lmp_row][lmp_column]
        position_type = position.position_type

        if position_type == "corner":
            return StateChecker._corner_mill_check(position)

        elif position_type == "connecting":
            return StateChecker._connecting_mill_check()

    @staticmethod
    def _corner_mill_check(position):
        mill = False
        next_pos = StateChecker._clear_invalid_positions(position.next)

        for next_position in next_pos.keys():
            adjacent = next_pos[next_position]
            if adjacent.piece == position.piece:
                next_adjacent = adjacent.next[next_position]
                if next_adjacent.piece == position.piece:
                    mill = True

        return mill

    @staticmethod
    def _connecting_mill_check(position):
        mill = False
        next_pos = position.next
        adjacent_opposite = {"right": "left", "left": "right", "up": "down", "down": "up"}

        for next_position in next_pos.keys():
            adjacent = next_pos[next_position]
            opposite = next_pos[adjacent_opposite[next_position]]
            if adjacent == position and

    @staticmethod
    def _clear_invalid_positions(position_dict):
        for next_position in position_dict.keys():
            if next_position is None:
                del position_dict[next_position]

        return position_dict






    @staticmethod
    def is_position_occupied(row, column):
        board_state = GameboardService().get_gameboard_state()
        return board_state[row][column].piece != 'o'
