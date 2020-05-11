from interface.ascii_art import art
from interface.exit_check import exit
from interface.start_game import start_game
from interface.clear_screen import clear_screen
from time import sleep


def splash_screen():
    made_by = "Ilija Kalinic"
    game_name = "Nine Men's Morris"
    print("{0:=^60}\nMade by:{1:=>52}".format(game_name, made_by))
    print(art)


def print_game_options():
    print("{:=^60}".format("Choose which type of game do you want to play:") +
          "\n\n1 - Human vs Human\n\n"
          "2 - Human vs Bot\n\n"
          "Enter - exit")


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
