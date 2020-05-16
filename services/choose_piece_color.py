from interface.piece_chooser_menu import piece_chooser_menu
from modules.coin import toss

def choose_piece_color():
    option = piece_chooser_menu()

    if option is None:
        return

    elif option == "R":
        return choose_random()

    else:
        return option


def choose_random():

        if toss() == "heads":
            return "W"
        else:
            return "B"
