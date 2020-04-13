class GameboardPositions(object):

    def __init__(self, positions):
        self._array = ["●" for position in range(positions)]
        self._num_of_positions = positions

    def __str__(self):
        return str(self._array)

    @property
    def array(self):
        return self._array

    @property
    def num_of_positions(self):
        return self._num_of_positions




def print_game_board(position_array):

    board = f"""
{position_array[0]}————————————————————{position_array[1]}————————————————————{position_array[2]}
|                    |                    |
|                    |                    |
|      {position_array[3]}—————————————{position_array[4]}—————————————{position_array[5]}      |
|      |             |             |      |
|      |             |             |      |
|      |      {position_array[6]}——————{position_array[7]}——————{position_array[8]}      |      |
|      |      |             |      |      |
|      |      |             |      |      |
{position_array[9]}——————{position_array[10]}——————{position_array[11]}             {position_array[12]}——————{position_array[13]}——————{position_array[14]}
|      |      |             |      |      |
|      |      |             |      |      |
|      |      {position_array[15]}——————{position_array[16]}——————{position_array[17]}      |      |
|      |             |             |      |
|      |             |             |      |
|      {position_array[18]}—————————————{position_array[19]}—————————————{position_array[20]}      |
|                    |                    |
|                    |                    |
{position_array[21]}————————————————————{position_array[22]}————————————————————{position_array[23]}"""

    between_3 = f"{'|':<21}|{'|':>21}"

    between_5 = f"{'|':<7}{'|':<14}|{'|':>14}{'|':>7}"

    between_7 =f"{'|':<7}{'|':<7}{'|':<14}{'|':>7}{'|':>7}"

    long_3_in_row = f""

    medium_3_in_row = f""

    small_3_in_row = f""

    six_in_row = f""



    print(board)
    # "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
    # "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
    # "O", "O",


if __name__ == '__main__':

    gameboard = GameboardPositions()

    print_game_board(gameboard.array)