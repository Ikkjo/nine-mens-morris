from re import match

from interface.invalid_position_inputs import invalid_position_inputs
from services.player_service import PlayerService

from services.state_checker import StateChecker


def matches(input_str):
    return match("[A-G][1-7]", input_str)

def check_init_input_and_convert_position(input_str):
    if not matches(input_str):
        raise TypeError("String doesn't match")

    if input_str in invalid_position_inputs:
        raise IndexError("Invalid position")

    position = PlayerService().input_conversion(input_str)

    if StateChecker().is_position_occupied(position[0],position[1]):
        raise ValueError("Position is occupied")

    return position

def check_mill_input_and_convert_position(input_str):
    if not matches(input_str):
        raise TypeError("String doesn't match")

    if input_str in invalid_position_inputs:
        raise IndexError("Invalid position")

    position = PlayerService().input_conversion(input_str)

    if not StateChecker().is_remove_legal(position[0],position[1]):
        raise ValueError("Remove isn't legal")

    return position


