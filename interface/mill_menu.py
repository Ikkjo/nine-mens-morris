from interface.display_active_player import display_active_player
from interface.draw_gameboard import draw_gameboard
from interface.clear_screen import clear_screen
from scripts.position_format import check_mill_input_and_convert_position


def mill_menu():
    clear_screen()
    draw_gameboard()
    display_active_player()
    while True:
        position = input("Mill! Choose which piece you want to remove ([A-G][1-7]\n>>>").upper()
        try:
            return check_mill_input_and_convert_position(position)

        except TypeError:
            print("Input format doesn't match!\n")

        except IndexError:
            print("Invalid position!\n")

        except ValueError:
            print("You may not remove that piece!\n")