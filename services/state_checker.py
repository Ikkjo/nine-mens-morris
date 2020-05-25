from services.gameboard_service import GameboardService
from repos.active_player import ActivePlayer


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
            return StateChecker._connecting_mill_check(position)

        elif position_type == "border":
            return StateChecker._border_mill_check(position)

    @staticmethod
    def _corner_mill_check(position):
        mill = False
        next_pos = StateChecker._clear_invalid_positions(position.next)

        for next_position in next_pos.keys():
            adjacent = next_pos[next_position]
            if position == adjacent:
                next_adjacent = adjacent.next[next_position]
                if position == next_adjacent:
                    mill = True

        return mill

    @staticmethod
    def _connecting_mill_check(position):
        mill = False
        next_pos = position.next
        adjacent_opposite = {"right": "left", "up": "down"}
        positions = ["up", "right"]

        for next_position in positions:
            adjacent = next_pos[next_position]
            opposite = next_pos[adjacent_opposite[next_position]]
            if adjacent == position and opposite == position:
                mill = True

        return mill

    @staticmethod
    def _border_mill_check(position):
        direction_axis = {"vertical": 0, "horizontal": 0}
        next_pos = StateChecker._clear_invalid_positions(position.next)

        for direction in next_pos.keys():
            if direction == "up" or direction == "down":
                direction_axis["vertical"] += 1
            elif direction == "left" or direction == "right":
                direction_axis["horizontal"] += 1

        for direction in direction_axis.keys():
            if direction_axis[direction] == 2:
                if direction == "horizontal":
                    if position.left == position and position.right == position:
                        return True

                else:
                    if position.up == position and position.down == position:
                        return True

            elif direction_axis[direction] == 2:
                if direction == "horizontal":
                    for dir in ["left", "right"]:
                        if dir in next_pos:
                            adjacent = next_pos[dir]
                            next_adjacent = adjacent.next[dir]
                            if position == adjacent and position == next_adjacent:
                                return True

                else:
                    for dir in ["up", "down"]:
                        if dir in next_pos:
                            adjacent = next_pos[dir]
                            next_adjacent = adjacent.next[dir]
                            if position == adjacent and position == next_adjacent:
                                return True

    @staticmethod
    def _clear_invalid_positions(position_dict):
        return_dict = {}
        for next_position in position_dict.keys():
            if position_dict[next_position] is not None:
                return_dict[next_position] = position_dict[next_position]

        return return_dict

    @staticmethod
    def is_remove_legal(row, column):
        legal = True
        active_player = ActivePlayer().player
        gameboard_state = GameboardService().gameboard.state

        if not StateChecker.is_position_occupied(row, column):
            legal = False

        if StateChecker.is_piece_color_equal(gameboard_state, row, column, active_player.piece_color):
            legal = False

        if StateChecker.is_piece_in_mill(gameboard_state, row, column):
            legal = False

        return legal

    @staticmethod
    def is_position_occupied(row, column):
        board_state = GameboardService().get_gameboard_state()
        return board_state[row][column].piece != 'o'

    @staticmethod
    def is_piece_in_mill(gameboard_state, row: int, column: int):
        position = (row, column)
        return StateChecker.check_mills(gameboard_state, position)

    @staticmethod
    def is_piece_color_equal(gameboard_state, row, column, piece_color):
        return gameboard_state[row][column] == piece_color
