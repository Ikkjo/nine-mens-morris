between_wide = f"{'|':<21}|{'|':>21}"

between_medium = f"{'|':<7}{'|':<14}|{'|':>14}{'|':>7}"

between_narrow = f"{'|':<7}{'|':<7}{'|':<14}{'|':<7}{'|':<7}|"

def wide_3(l, m, r):
    return f"{l:—<21}{m}{r:—>21}"


def medium_3(l, m, r):
    return f"{'|':<7}{l:—<14}{m}{r:—>14}{'|':>7}"


def narrow_3(l, m, r):
    return f"{'|':<7}{'|':<7}{l:—<7}{m}{r:—>7}{'|':>7}{'|':>7}"


def middle_left(l, m, r):
    return f"{l:—<7}{m}{r:—>7}{' ':13}"


def middle_right(l, m, r):
    return f"{l:—<7}{m}{r:—>7}"


def three_rows(board_state, symmetry):

    if not symmetry:
        wide_row = board_state[0]

        medium_row = board_state[1]

        narrow_row = board_state[2]

        wide = wide_3(wide_row['l'], wide_row['m'], wide_row['r']) + '\n' +\
               (between_wide + '\n')* 2

        medium = medium_3(medium_row['l'], medium_row['m'], medium_row['r']) + '\n' +\
                 (between_medium + '\n') * 2

        narrow = narrow_3(narrow_row['l'], narrow_row['m'], narrow_row['r']) + '\n' +\
                 (between_narrow + '\n') * 2

    else:
        wide_row = board_state[5]

        medium_row = board_state[6]

        narrow_row = board_state[7]

        wide = (between_wide + '\n') * 2 +\
               wide_3(wide_row['l'], wide_row['m'], wide_row['r']) + '\n'


        medium = (between_medium + '\n') * 2 +\
                 medium_3(medium_row['l'], medium_row['m'], medium_row['r']) + '\n'


        narrow = (between_narrow + '\n') * 2 +\
                 narrow_3(narrow_row['l'], narrow_row['m'], narrow_row['r']) + '\n'

    return wide + medium + narrow if not symmetry else narrow + medium + wide


def middle_row(board_state):
    left = board_state[3]

    right = board_state[4]

    middle = middle_left(left['l'], left['m'], left['r']) + middle_right(right['l'], right['m'], right['r']) + '\n'

    return middle


def pretty_game_board(board_state, yellow_background=False):

    ansi_ylw_start = '\033[43m' if yellow_background else ''

    ansi_ylw_end = '\033[0m' if yellow_background else ''

    first_half = three_rows(board_state, symmetry=False)

    middle = middle_row(board_state)

    second_half = three_rows(board_state, symmetry=True)

    return ansi_ylw_start + first_half + middle + second_half + ansi_ylw_end


# if __name__ == '__main__':
#
#     pos_dict = {'l': 'W', 'm': '●', 'r': 'B'}
#
#     board_state = [pos_dict for row in range(8)]# [["●" for position in range(3)] for row in range(7)]
#
#
#     board_state[1]['m'].replace('●', '□')
#
#
#     print(pretty_game_board(board_state))