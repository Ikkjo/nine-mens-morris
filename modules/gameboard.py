from interface.gameboard_print import pretty_game_board
from modules.singleton_metaclass import Singleton
from modules.position import Position


class Gameboard(object, metaclass=Singleton):
    _num_of_positions = 24
    _max_columns = 3
    _max_rows = 8

    def __init__(self):
        state = list()
        for row in range(self.max_rows):
            pos = list()
            for column in range(self.max_columns):
                pos.append(Position(row, column))
            state.append(pos)

        initialised_state = self._set_pos_refs()

        self.state = initialised_state

    def __str__(self):
        return pretty_game_board(self.state)

    @staticmethod
    def _set_pos_refs(state: list):
        None

        return initialised_state

    @property
    def num_of_positions(self):
        return self._num_of_positions

    @property
    def max_columns(self):
        return self._max_columns

    @property
    def max_rows(self):
        return self._max_rows
