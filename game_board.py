def print_game_board():
    board = """●————————————————————●————————————————————●
|                    |                    |
|                    |                    |
|      ●—————————————●—————————————●      |
|      |             |             |      |
|      |             |             |      |
|      |      ●——————●——————●      |      |
|      |      |             |      |      |
|      |      |             |      |      |
●——————●——————●             ●——————●——————●
|      |      |             |      |      |
|      |      |             |      |      |
|      |      ●——————●——————●      |      |
|      |             |             |      |
|      |             |             |      |
|      ●—————————————●—————————————●      |
|                    |                    |
|                    |                    |
●————————————————————●————————————————————●"""

    print(board)

def print_box(side):



    for row in range(side):

        for column in range(side):
            if (row == 0 or row == side-1) or (column == 0 or column == side-1):
                if row == 0:
                    if column == 0:
                        print("┏", end='')

                    elif column == side-1:
                        print("┓", end="\n")

                    else:
                        print("━", end='')

                elif row == side-1:
                    if column == 0:
                        print("┗", end='')

                    elif column == side-1:
                        print("┛")

                    else:
                        print("━", end='')

                else:
                    if column == 0 or column == side-1:

                        end = '\n' if column == side - 1 else ''

                        print("┃", end=end)

                    print(" "*side, end='')






if __name__ == '__main__':
    print_box(20)