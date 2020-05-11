from modules.piece import Piece

class Player(object):

    starting_pieces = 9

    def init(self, color):
        piece_list = list()

        for piece in range(self.starting_pieces):

            piece_list.append(Piece())