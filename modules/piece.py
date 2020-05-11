class Piece(object):

    possible_pieces = ("B", "W")

    def __init__(self, color, position=None):
        self.piece = self.possible_pieces[color]
        self.position = position
        self._next_position = {"right": None, "left": None,
                     "up": None, "down": None}

    def __str__(self):
        return self.piece

    @property
    def right(self):
        return self._next_position["right"]
    # setters for properties maybe redundant
    @right.setter
    def right(self, new_right_piece):
        self._next_position["right"] = new_right_piece
        
    @property
    def left(self):
        return self._next_position["left"]
    
    @left.setter
    def left(self, new_left_piece):
        self._next_position["left"] = new_left_piece
    
    @property
    def up(self):
        return self._next_position["up"]
    
    @up.setter
    def up(self, new_up_piece):
        self._next_position["up"] = new_up_piece
    
    @property
    def down(self):
        return self._next_position["down"]
    
    @down.setter
    def down(self, new_down_piece):
        self._next_position["down"] = new_down_piece

    def piece_type(self):
        """Method for defining piece type

        If the piece type is "connecting" that means it is adjacent to 4 positions on the board and can directly move
        to them, in this game (Nine Mens Morris) that means the piece is on the middle box (if you look at the gameboard
        it looks like there are three connected boxes, decreasing in size, one inside the other). If the type is
        "border" then the piece is either in the inside or the outside box, on one of the four sides (not the corner).
        If the type is "corner" then the piece can be on any of the four vertices on any of the 3 boxes.

        Returns:
            p_type (str): type of the piece, can either be "corner", "connecting" or "border"
        """
        check = list()
        check.append(self._next_position["right"])
        check.append(self._next_position["left"])
        check.append(self._next_position["up"])
        check.append(self._next_position["down"])

        unavailable_pos = 0

        for next_position in check:
            if next_position is None:
                unavailable_pos += 1

        p_type = None

        if unavailable_pos == 0:
            p_type = "connecting"

        elif unavailable_pos == 1:
            p_type = "border"

        elif unavailable_pos == 2:
            p_type = "corner"

        if p_type is None:
            raise TypeError("Type of piece error (number of next positions is invalid)!")

        return p_type
