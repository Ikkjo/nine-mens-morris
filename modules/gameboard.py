from interface.gameboard_print import pretty_game_board
from modules.singleton_metaclass import Singleton


# TODO: Make Gameboard a singleton class


class Gameboard(object, metaclass=Singleton):
    _num_of_positions = 24
    _max_columns = 3
    _max_rows = 8

    def __init__(self):
        state = []
        for row in range(self.max_rows):
            pos = []
            for column in range(self.max_columns):
                pos.append(Position(row, column))
            state.append(pos)

        self.state = state

    def __str__(self):
        return pretty_game_board(self.state)

    @property
    def num_of_positions(self):
        return self._num_of_positions

    @property
    def max_columns(self):
        return self._max_columns

    @property
    def max_rows(self):
        return self._max_rows

class Position(object):

    def __init__(self, row, column, piece=None):
        self.piece = piece if piece is not None else "●"
        self.row = row
        self.column = column

    def __str__(self):
        return self.piece
