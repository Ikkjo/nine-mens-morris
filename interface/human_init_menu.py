from scripts.position_format import check_input


def init_menu():
    while True:
        position = input("Where do you want to put your piece? ([A-G][1-7])\n>>>").upper()
        try:
            position = check_input(position)
            return position

        except TypeError:
            print("Input doesn't match format!")

        except IndexError:
            print("You can't put your piece there!")

        except ValueError:
            print("That position is occupied!")