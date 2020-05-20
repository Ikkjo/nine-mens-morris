between_wide = f"{'|':<21}|{'|':>21}"

between_medium = f"{'|':<7}{'|':<14}|{'|':>14}{'|':>7}"

between_narrow = f"{'|':<7}{'|':<7}{'|':<14}{'|':<7}{'|':<7}|"

def wide_3(l, m, r):
    return f"{l.piece:—<21}{m.piece}{r.piece:—>21}"


def medium_3(l, m, r):
    return f"{'|':<7}{l.piece:—<14}{m.piece}{r.piece:—>14}{'|':>7}"


def narrow_3(l, m, r):
    return f"{'|':<7}{'|':<7}{l.piece:—<7}{m.piece}{r.piece:—>7}{'|':>7}{'|':>7}"


def middle_left(l, m, r):
    return f"{l.piece:—<7}{m.piece}{r.piece:—>7}{' ':13}"


def middle_right(l, m, r):
    return f"{l.piece:—<7}{m.piece}{r.piece:—>7}"


def three_rows(board_state, symmetry):

    if not symmetry:
        wide_row = board_state[0]

        medium_row = board_state[1]

        narrow_row = board_state[2]

        wide = wide_3(wide_row[0], wide_row[1], wide_row[2]) + '\n' +\
               (between_wide + '\n')* 2

        medium = medium_3(medium_row[0], medium_row[1], medium_row[2]) + '\n' +\
                 (between_medium + '\n') * 2

        narrow = narrow_3(narrow_row[0], narrow_row[1], narrow_row[2]) + '\n' +\
                 (between_narrow + '\n') * 2

    else:
        wide_row = board_state[7]

        medium_row = board_state[6]

        narrow_row = board_state[5]

        wide = (between_wide + '\n') * 2 +\
               wide_3(wide_row[0], wide_row[1], wide_row[2]) + '\n'


        medium = (between_medium + '\n') * 2 +\
                 medium_3(medium_row[0], medium_row[1], medium_row[2]) + '\n'


        narrow = (between_narrow + '\n') * 2 +\
                 narrow_3(narrow_row[0], narrow_row[1], narrow_row[2]) + '\n'

    return wide + medium + narrow if not symmetry else narrow + medium + wide


def middle_row(board_state):
    left = board_state[3]

    right = board_state[4]

    middle = middle_left(left[0], left[1], left[2]) + middle_right(right[0], right[1], right[2]) + '\n'

    return middle


def pretty_game_board(board_state):

    first_half = three_rows(board_state, symmetry=False)

    middle = middle_row(board_state)

    second_half = three_rows(board_state, symmetry=True)

    return first_half + middle + second_half


# if __name__ == '__main__':
#
#     pos_dict = {0: 'W', 1: '●', 2: 'B'}
#
#     board_state = [pos_dict for row in range(8)]# [["●" for position in range(3)] for row in range(7)]
#
#
#     board_state[1][1].replace('●', '□')
#
#
#     print(pretty_game_board(board_state))