from interface.piece_chooser_menu import piece_chooser_menu
from interface.exit_check import exit

def choose_piece_color():
    option = piece_chooser_menu()

    if option is None:
        return
