from interface.clear_screen import clear_screen
from interface.exit_check import exit


def print_game_options():
    print("|>{:^60}<|".format("Choose which type of game you want to play") +
          "\n\n" + "{:^60}".format("1 - Human vs Human") + "\n\n"
          "{:^60}".format("2 - Human vs Bot") + "\n\n\n\n"
          "{:>60}".format("Enter - exit") + "\n\n")


def starting_menu():
    options = {"1": "human",
               "2": "bot"}

    while True:
        clear_screen()
        print_game_options()

        mode = input(">>>")
        if exit(mode):
            return None

        if mode in options:
            return options[mode]
