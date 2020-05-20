from interface.clear_screen import clear_screen
from interface.exit_check import exit


def colour_chooser_menu():
    valid_options = {"B", "W", "R"}

    while True:

        clear_screen()

        print_piece_options()

        option = input(">>>").upper()

        if exit(option):
            return None

        if option in valid_options:
            return option


def print_piece_options():
    print("|>{:^60}<|".format("Choose your preffered piece color") +
          "\n\n" + "{:^60}".format("B - Black") + "\n\n"
                   "{:^60}".format("W - White") + "\n\n"
                   "{:^60}".format("R - I don't know, toss a coin! (Random)") + "\n\n\n\n"
                   "{:>60}".format("Enter - exit") + "\n\n")