class Gameboard(object):

    def __init__(self):
        self._num_of_positions = 24
        self._array = ["●" for position in range(24)]


    def __str__(self):
        return str(self._array)

    @property
    def array(self):
        return self._array

    @property
    def num_of_positions(self):
        return self._num_of_positions


if __name__ == '__main__':

    gameboard = Gameboard()

    print_game_board(gameboard.array)