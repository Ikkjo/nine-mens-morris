from scripts.position_format import check_input


def human_init():
    while True:
        position = input("Where do you want to put your piece? ([A-G][1-7])\n>>>")
        try:
            position = check_input(position)
            return position

        except TypeError:
            print("Input doesn't match format!")

        except IndexError:
            print("You can't put your piece there!")

        except ValueError:
            print("That position is occupied!")

