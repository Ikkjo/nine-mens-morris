from interface.clear_screen import clear_screen
from interface.display_winner import display_winner
from interface.splash_screen import splash_screen
from interface.starting_menu import starting_menu
from scripts.play_game import play_game


def game():
    clear_screen()
    splash_screen()

    while True:

        clear_screen()

        mode = starting_menu()

        if mode is None:
            return

        winner = play_game(mode)
        display_winner(winner)
