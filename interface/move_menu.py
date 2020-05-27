from scripts.position_format import check_move_piece_input_and_convert_position, check_move_position_input_and_convert_position


def move_menu():

    piece = get_move_piece()
    position = get_move_position(piece)
    return (piece, position)


def get_move_piece():
    while True:
        piece = input("Which piece do you want to move? ([A-G][1-7])\n>>>")
        try:
            return check_move_piece_input_and_convert_position(piece)

        except TypeError:
            print("Input doesn't match format!")

        except IndexError:
            print("Position doesn't exist!")

        except ValueError:
            print("That isn't your piece!")


def get_move_position(piece):
    while True:
        position = input("Where do you want to move your piece? ([A-G][1-7])\n>>>")
        try:
            return check_move_position_input_and_convert_position(position, piece)

        except TypeError:
            print("Input doesn't match format!")

        except IndexError:
            print("Position doesn't exist!")

        except ValueError:
            print("Illegal move!")