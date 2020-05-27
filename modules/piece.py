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
        self._piece_color = color

        self.position = None

    def __str__(self):
        return self._piece_color

    def __eq__(self, other):
        if isinstance(other, Piece):
            return self._piece_color == other.piece_color
        elif isinstance(other, str):
            return self._piece_color == other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Piece):
            return self._piece_color != other.piece_color
        elif isinstance(other, str):
            return self._piece_color != other
        else:
            return True

    @property
    def piece_color(self):
        return self._piece_color
