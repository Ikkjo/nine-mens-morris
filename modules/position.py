class Position(object):

    def __init__(self, row, column, piece=None):
        self.row = row
        self.column = column
        self.piece = piece if piece is not None else "o"
        self.right = None
        self.up = None
        self.left = None
        self.down = None

    def __str__(self):
        return str(self.piece)

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.piece == other.piece
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Position):
            return self.piece != other.piece
        else:
            return True

    @property
    def next(self):
        return {"up": self.up, "down": self.down, "left": self.left, "right": self.right}

    # Method below (piece_type) may not be needed
    def position_type(self):
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
        check.append(self.right)
        check.append(self.up)
        check.append(self.left)
        check.append(self.down)

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

    @property
    def has_up(self):
        return self.up is not None

    @property
    def has_down(self):
        return self.down is not None

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    def has(self, direction):
        directions = {"up": self.up is not None,
                      "down": self.down is not None,
                      "left": self.left is not None,
                      "right": self.right is not None}

        return directions[direction]

    @property
    def is_blocked(self):
        next_positions = []
        for direction in self.next.keys():
            if self.next[direction] is not None:
                next_positions.append(self.next[direction])

        for adjacent in next_positions:
            if adjacent.piece == 'o':
                return False

        return True

