def wide_3(l, m, r):
    return f"{l:—<21}{m}{r:—>21}"


def medium_3(l, m, r):
    return f"{'|':<7}{l:—<14}{m}{r:—>14}{'|':>7}"


def narrow_3(l, m, r):
    return f"{'|':<7}{'|':<7}{l:—<7}{m}{r:—>7}{'|':>7}{'|':>7}"


def middle_l(l, m, r):
    return f"{l:—<7}{m}{r:—>7}{' ':13}"


def middle_r(l, m, r):
    return f"{l:—<7}{m}{r:—>7}"


def print_game_board(position_array):
    between_3 = f"{'|':<21}|{'|':>21}"

    between_5 = f"{'|':<7}{'|':<14}|{'|':>14}{'|':>7}"

    between_6 = f"{'|':<7}{'|':<7}{'|':<14}{'|':<7}{'|':<7}|"

    long_3_in_row = f"{position_array[0]:—<21}{position_array[0]}{position_array[0]:—>21}"

    medium_3_in_row = f"{'|':<7}{position_array[0]:—<14}{position_array[0]}{position_array[0]:—>14}{'|':>7}"

    small_3_in_row = f"{'|':<7}{'|':<7}{position_array[0]:—<7}{position_array[0]}{position_array[0]:—>7}{'|':>7}{'|':>7}"

    L_six_in_row = f"{position_array[0]:—<7}{position_array[0]}{position_array[0]:—>7}{' ':13}"

    R_six_in_row = f"{position_array[0]:—<7}{position_array[0]}{position_array[0]:—>7}"

    printing_order = {1: long_3_in_row}
