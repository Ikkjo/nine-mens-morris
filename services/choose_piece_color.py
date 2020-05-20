from interface.colour_chooser_menu import colour_chooser_menu
from modules.coin import toss


def choose_piece_color():
    option = colour_chooser_menu()

    if option is None:
        return

    elif option == "R":
        return choose_random()

    elif option == "W" or option == "B":
        return option


def choose_random():
    if toss() == "heads":
        return "W"
    else:
        return "B"


def second_player_piece_color(first_player_piece_color):
    return "W" if first_player_piece_color == "B" else "B"
