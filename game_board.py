from gameboard_print import pretty_game_board
from piece import Piece

# TODO: Make Gameboard a singleton class


class Gameboard(object):

    num_of_positions = 24
    max_columns = 3
    max_rows = 8

    def __init__(self):
        # self.state = [{"l": "●", "m": "●", "r": "●"} for position in range(self._num_of_positions)]
        state = []
        for row in range(self.max_rows):
            pos = []
            for column in range(self.max_columns):
                pos.append("●")
            state.append(pos)

        self.state = state

    def __str__(self):
        return pretty_game_board(self.state)

    def check_rows(self, row):
        return row <= self.max_rows

    def check_columns(self, column):
        return column <= self.max_columns

    def check_pos_index(self, row, column):
        if (self.check_rows(row) and self.check_columns(column)) is False:
            raise IndexError("Position out of bounds!")

    def set_piece_to_pos(self, row, column, piece):
        self.check_pos_index(row, column)
        self.state[row][column] = piece

    def get_piece_from_pos(self, row, column):
        self.check_pos_index(row, column)
        return self.state[row][column]

class Position(object):

    def __init__(self, row, column, piece=None):
        self.piece = piece if piece is not None else "●"
        self.row = row
        self.column = column

if __name__ == '__main__':

    gb = Gameboard()

    w1 = Piece(1)
    w2 = Piece(1)

    gb.set_piece_to_pos(2, 1, w1)
    gb.set_piece_to_pos(3, 1, w2)
    gb.set_piece_to_pos(7, 0, "B")

    a = gb.get_piece_from_pos(2, 1)

    print(gb, a)


