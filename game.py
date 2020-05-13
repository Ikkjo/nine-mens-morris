from interface.clear_screen import clear_screen
from interface.starting_menu import starting_menu
from services.play_game import play_game


def game():
    clear_screen()
    mode = starting_menu()
    if mode is None:
        return
    play_game(mode)






