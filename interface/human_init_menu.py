from scripts.position_format import check_init_input_and_convert_position


def init_menu():
    while True:
        position = input("Where do you want to put your piece? ([A-G][1-7])\n>>>").upper()
        try:
            position = check_init_input_and_convert_position(position)
            return position

        except TypeError:
            print("Input doesn't match format!")

        except IndexError:
            print("You can't put your piece there!")

        except ValueError:
            print("That position is occupied!")