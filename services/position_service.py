from modules.position import Position


class PositionService(object):
    """This object should ideally be called once at the start of the game,
     during the initialization of the game board"""

    ref_reverses = {"up": "down",
                    "down": "up",
                    "left": "right",
                    "right": "left"}

    @staticmethod
    def change_reference(position: Position, new_reference: Position, reference):
        """Changes positions up reference to a new position, also changes the new positions down reference

        Args:
            position: position for which we want to change the up reference to
            new_up_reference: the position obj which position.up is referencing

        Raises:
            TypeError if reference is not in {"up", "down", "left", "right"}, or if position or new_reference are not
            type Position


        """

        refs = {"up": PositionService._change_up,
                "down": PositionService._change_down,
                "left": PositionService._change_left,
                "right": PositionService._change_right}

        if reference not in refs or (isinstance(position, Position) and isinstance(new_reference, Position)):
            raise TypeError("A serious error has occurred...")



    @staticmethod
    def _change_up(position: Position, new_reference):
        position.up = new_reference

    @staticmethod
    def _change_down(position: Position, new_reference):
        position.down = new_reference

    @staticmethod
    def _change_left(position: Position, new_reference):
        position.left = new_reference

    @staticmethod
    def _change_right(position, new_reference):
        position.right = new_reference