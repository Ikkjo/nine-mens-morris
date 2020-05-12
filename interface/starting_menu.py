from time import sleep

from interface.ascii_art import art
from interface.clear_screen import clear_screen
from interface.exit_check import exit


def splash_screen():
    made_by = "Ilija Kalinić"
    game_name = "Nine Men's Morris"
    print("{0:#^60}\nMade by:{1:#>52}".format(game_name, made_by))
    print("{:^60}".format(art))


def print_game_options():
    print("|>{:^60}<|".format("Choose which type of game you want to play") +
          "\n\n" + "{:^60}".format("1 - Human vs Human") + "\n\n"
          "{:^60}".format("2 - Human vs Bot") + "\n\n\n\n"
          "{:>60}".format("Enter - exit") + "\n\n")


def starting_menu():
    options = {"1": "human",
               "2": "bot"}

    splash_screen()
    sleep(5)

    while True:
        clear_screen()
        print_game_options()

        mode = input(">>>")
        if exit(mode):
            break

        if mode in options:
            return options[mode]
