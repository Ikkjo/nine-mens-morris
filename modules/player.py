from modules.piece import Piece


class HumanPlayer(object):

    starting_pieces = 9

    def __init__(self, color: int):
        piece_list = list()

        for piece in range(self.starting_pieces):

            piece_list.append(Piece(color))

        self.pieces_unused_list = piece_list
        self.piece_list = list()

    @property
    def pieces_left(self):
        return len(self.piece_list) + len(self.pieces_unused_list)