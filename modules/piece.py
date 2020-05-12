class Piece(object):

    possible_pieces = ("B", "W")

    def __init__(self, color, position=None):
        self.piece = self.possible_pieces[color]
        self.position = position

    def __str__(self):
        return self.piece
