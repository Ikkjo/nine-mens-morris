from modules.position import Position


class PositionService(object):
    """This object should ideally be called once at the start of the game,
     during the initialization of the game board"""



    @staticmethod
    def make_reference(position: Position, new_reference: Position, reference):
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

        ref_reverses = {"up": "down",
                        "down": "up",
                        "left": "right",
                        "right": "left"}

        # TODO: Fix error bug
        # Unknown reason for bug, TypeError is raised even when condition is true
        # if reference not in refs or (isinstance(position, Position) and isinstance(new_reference, Position)):
        #     raise TypeError("A serious error has occurred...")

        new_pos = refs[reference](position, new_reference)
        new_ref_pos = refs[ref_reverses[reference]](new_reference, position)

        ret_val = (new_pos, new_ref_pos)

        return ret_val

    @staticmethod
    def _change_up(position: Position, new_reference):
        position.up = new_reference
        return position

    @staticmethod
    def _change_down(position: Position, new_reference):
        position.down = new_reference
        return position

    @staticmethod
    def _change_left(position: Position, new_reference):
        position.left = new_reference
        return position

    @staticmethod
    def _change_right(position, new_reference):
        position.right = new_reference
        return position