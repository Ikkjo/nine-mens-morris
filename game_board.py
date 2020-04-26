from gameboard_print import pretty_game_board


def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")

class Gameboard(object):

    def __init__(self):
        self._num_of_positions = 24
        self._array = [{"l": "●", "m": "●", "r": "●"} for position in range(self._num_of_positions)]

    def __str__(self):
        return pretty_game_board(self._array)

    @property
    def array(self):
        return self._array

    @property
    def num_of_positions(self):
        return self._num_of_positions


if __name__ == '__main__':

    gameboard = Gameboard()
    print("\n" * 60)
    print(gameboard)
    input("input")
    print("\n"*60)
    print("\n" + str(gameboard))
    input()
    print("\n"*60)

