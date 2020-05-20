from modules.position import Position


class Piece(object):

    piece_colors = {"B", "W"}

    def __init__(self, color: str):
        """Inits piece

        Attributes:
            piece (str)
            position (Position)
        """
        if color not in self.piece_colors:
            raise TypeError("Invalid piece color!")
        self._piece = color

        self.position = None

    def __str__(self):
        return self._piece

    @property
    def piece(self):
        return self._piece
