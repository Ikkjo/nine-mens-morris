from services.state_checker import StateChecker
from modules.position import Position
from copy import deepcopy

def board_state_eval(best_move, player_color, mode):
    board_state = best_move.board_state
    if isinstance(best_move.last_played_move, tuple):
        moved_from_pos = best_move.last_played_move[0]
        last_played_move = best_move.last_played_move[1]

    elif isinstance(best_move.last_played_move, Position):
        last_played_move = best_move.last_played_move

    phase_coefs = {"INIT": [14, 37, 4, 14, 20, 2],
                  "MOVE": [16, 43, 11, 8, 7, 42, 1086],
                  "FLY": [10, 1, 16, 1190]}

    evaluation = 0

    if mode == "INIT":
        init_coefs = phase_coefs["INIT"]
        config_nums = configs(board_state, player_color, move_phase=False)
        closed_m = closed_morris(board_state, player_color, last_played_move)*init_coefs[0]
        morris_num = config_nums["morrises"] * init_coefs[1]
        blocked_num = blocked_number(board_state, player_color)*init_coefs[2]
        piece_num = pieces_number(board_state, player_color)*init_coefs[3]
        two_piece = config_nums["two_piece"] * init_coefs[4]
        three_piece = config_nums["three_piece"] * init_coefs[5]

        evaluation = closed_m + morris_num + blocked_num + piece_num + two_piece + three_piece

    elif mode == "MOVE":
        move_coefs = phase_coefs["MOVE"]
        config_nums = configs(board_state, player_color, last_played_move)
        closed_m = closed_morris(board_state, player_color, last_played_move) * move_coefs[0]
        morris_num = config_nums["morrises"] * move_coefs[1]
        blocked_num = blocked_number(board_state, player_color) * move_coefs[2]
        piece_num = pieces_number(board_state, player_color) * move_coefs[3]
        opened_m = opened_morris(board_state, player_color, moved_from_pos) * move_coefs[4]
        double_m = config_nums["double_morris"] * move_coefs[5]
        winning = winning_configuration(board_state, player_color, last_played_move) * move_coefs[6]

        evaluation = closed_m + morris_num + blocked_num + piece_num + opened_m + double_m + winning

    elif mode == "FLY":
        fly_coefs = phase_coefs["FLY"]
        config_nums = configs(board_state, player_color, last_played_move)

        two_piece = config_nums["two_piece"] * fly_coefs[4]
        three_piece = config_nums["three_piece"] * fly_coefs[5]
        closed_m = closed_morris(board_state, player_color, last_played_move) * fly_coefs[0]
        winning = winning_configuration(board_state, player_color, last_played_move) * fly_coefs[6]


    return evaluation


def closed_morris(board_state, player_color, last_played_move):

    closed_morris = 0

    if StateChecker().check_mill(board_state, last_played_move):
        if last_played_move.piece == player_color:
            closed_morris += 1
        else:
            closed_morris -= 1


    return closed_morris

def blocked_number(board_state, player_color):



    blocked_pieces = 0

    for row in board_state:
        for position in row:
            if position.piece != "o" and position.is_blocked:
                if position.piece == player_color:
                    blocked = 1
                else:
                    blocked = -1

                blocked_pieces += blocked

    return blocked_pieces


def pieces_number(board_state, player_color):



    rows = range(len(board_state))
    columns = range(len(board_state[0]))

    your_color = player_color
    oponents_color = 'W' if player_color == 'B' else 'B'

    difference = 0

    for row in rows:
        for column in columns:
            position = board_state[row][column]
            if position.piece == 'o':
                continue
            if position.piece.piece_color == your_color:
                difference += 1
            elif board_state[row][column].piece.piece_color == oponents_color:
                difference -= 1



    return difference

def configs(board_state, player_color, move_phase=False):
    opponent_color = "W" if player_color == "B" else "B"

    config_nums = {"three_piece": 0, "two_piece":0, "double_morrises":0, "morrises": 0, "pieces_num": 0}

    #  I cry every time I see this

    number = {player_color: 1,
              opponent_color: -1}

    visited_two_piece = []
    visited_morrrises = []

    vertical_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (5, 1)]

    horizontal_positions = [(0, 0), (1, 0), (4, 0), (3, 0), (6, 0), (2, 0), (5, 0), (7, 0)]

    for vert_pos, hor_pos in zip(vertical_positions, horizontal_positions):
        vert_row = vert_pos[0]
        vert_column = vert_pos[1]
        vertical_position = board_state[vert_row][vert_column]
        lower = vertical_position.down
        lowest = lower.down

        hor_row = hor_pos[0]
        hor_column = hor_pos[1]
        left = board_state[hor_row][hor_column]
        middle = left.right
        right = middle.right

        if vertical_position.piece == lower.piece and not isinstance(vertical_position.piece, str):
            config_nums["two_piece"] += number[vertical_position.piece.piece_color]
            visited_two_piece.append(vertical_position)
            visited_two_piece.append(lower)



        if vertical_position.piece == lowest.piece and not isinstance(vertical_position.piece, str):
            if lower not in visited_two_piece and vertical_position not in visited_two_piece:
                config_nums["two_piece"] += number[vertical_position.piece.piece_color]
                visited_two_piece.append(vertical_position)
                visited_two_piece.append(lowest)


            else:
                visited_two_piece.append(lowest)
                visited_morrrises.append(vertical_position)
                visited_morrrises.append(lower)
                visited_morrrises.append(lowest)
                config_nums["two_piece"] += number[vertical_position.piece.piece_color]
                config_nums["morrises"] += number[vertical_position.piece.piece_color]


        if left.piece == middle.piece and not isinstance(left.piece, str):
            config_nums["two_piece"] += number[left.piece.piece_color]
            visited_two_piece.append(left)
            visited_two_piece.append(middle)


        if left.piece == right.piece and not isinstance(left.piece, str):
            if left not in visited_two_piece and middle not in visited_two_piece:
                config_nums["two_piece"] += number[left.piece.piece_color]
                visited_two_piece.append(left)
                visited_two_piece.append(right)


            else:
                visited_two_piece.append(lowest)
                visited_morrrises.append(vertical_position)
                visited_morrrises.append(lower)
                visited_morrrises.append(lowest)
                config_nums["two_piece"] += number[left.piece.piece_color]
                config_nums["morrises"] += number[left.piece.piece_color]

    # Temporary fix
    # three_piece = count_triple_config(visited_two_piece, player_color, opponent_color, board_state,
    #                                  visited_morris=visited_morrrises)
    # config_nums["three_piece"] += three_piece

    if move_phase:
        double_morrises = count_triple_config(visited_morrrises, player_color, opponent_color, board_state)
        config_nums["double_morrises"] += double_morrises

    return config_nums


def count_triple_config(visited_two_piece, player_color, opponent_color, board_state, visited_morris=[]):

    triple = 0

    if len(visited_two_piece) != 0:
        number = {player_color: 1,
                  opponent_color: -1}
        for position in visited_two_piece:
            compare = visited_two_piece.remove(position)

            if position not in compare and position not in visited_morris:
                color = position.piece.piece_color
                triple += number[color]


    return triple


def opened_morris(board_state, player_color, moved_from_pos):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))
    opened = 0

    oponent_color = "W" if player_color == "B" else "B"


    if StateChecker.check_mill(board_state, moved_from_pos):
        if moved_from_pos.piece == player_color:
            opened += 1
        elif moved_from_pos.piece == oponent_color:
            opened -= 1


    return opened


def double_morris(board_state, player_color, last_played_move):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

    double = 0

    return double

def winning_configuration(board_state, player_color):
    oponents_color = "W" if player_color == "B" else "B"
    your_pieces = 0
    oponents_pieces = 0

    for row in board_state:
        for position in row:
            if position.piece != 'o':
                if position.piece == player_color:
                    your_pieces += 1
                elif position.piece == oponents_color:
                    oponents_pieces += 1

    winning = 0

    if oponents_pieces == 2:
        winning += 1

    elif your_pieces == 2:
        winning -= 1

    return winning
