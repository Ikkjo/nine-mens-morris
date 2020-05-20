class Position(object):

    def __init__(self, row, column, piece=None):
        self.row = row
        self.column = column
        self.piece = piece if piece is not None else "●"
        self._next_position = {"right": None, "left": None,
                               "up": None, "down": None}

    def __str__(self):
        return self.piece


    @property
    def right(self):
        return self._next_position["right"]

    # setters for properties maybe redundant
    @right.setter
    def right(self, new_right_reference):
        self._next_position["right"] = new_right_reference

    @property
    def left(self):
        return self._next_position["left"]

    @left.setter
    def left(self, new_left_reference):
        self._next_position["left"] = new_left_reference

    @property
    def up(self):
        return self._next_position["up"]

    @up.setter
    def up(self, new_up_reference):
        self._next_position["up"] = new_up_reference

    @property
    def down(self):
        return self._next_position["down"]

    @down.setter
    def down(self, new_down_reference):
        self._next_position["down"] = new_down_reference

    # Method below (piece_type) may not be needed

    def piece_type(self):
        """Method for defining piece type

        If the piece type is "connecting" that means it is adjacent to 4 positions on the board and can directly move
        to them, in this game (Nine Men's Morris) that means the piece is on the middle box (if you look at the
        gameboard it looks like there are three connected boxes, decreasing in size, one inside the other). If the type
        is "border" then the piece is either in the inside or the outside box, on one of the four sides (not the
        corner). If the type is "corner" then the piece can be on any of the four vertices on any of the 3 boxes.

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
