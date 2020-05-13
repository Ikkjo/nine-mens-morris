from interface.clear_screen import clear_screen
from interface.starting_menu import starting_menu


def game():
    clear_screen()
    mode = starting_menu()
    play_game(mode)






