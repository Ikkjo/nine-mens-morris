from modules.gameboard import Gameboard
from modules.piece import Piece


class GameboardService(object):

    def __init__(self):
        self.gameboard = Gameboard()

    def __str__(self):
        return self.gameboard.__str__()

    def check_rows(self, row):
        return row <= self.gameboard.max_rows

    def check_columns(self, column):
        return column <= self.gameboard.max_columns

    def check_pos_index(self, row, column):
        if (self.check_rows(row) and self.check_columns(column)) is False:
            raise IndexError("Position out of bounds!")

    def set_piece_to_pos(self, row, column, piece):
        self.check_pos_index(row, column)
        self.gameboard.state[row][column].piece.piece_color = piece

    def get_piece_from_pos(self, row, column):
        self.check_pos_index(row, column)
        return self.gameboard.state[row][column].piece.piece_color


if __name__ == '__main__':
    gbs = GameboardService()

    w1 = Piece(1)
    w2 = Piece(1)

    gbs.set_piece_to_pos(2, 1, w1)
    gbs.set_piece_to_pos(3, 1, w2)
    gbs.set_piece_to_pos(7, 0, "B")

    a = gbs.get_piece_from_pos(2, 1)

    print(gbs, a)
