from services.state_checker import StateChecker

def board_state_eval(best_move, player_color, mode):
    board_state = best_move.board_state
    last_played_move = best_move.last_played_move

    phase_coefs = {"INIT": [14, 37, 4, 14, 20, 2],
                  "MOVE": [16, 43, 11, 8, 7, 42, 1086],
                  "FLY": [10, 1, 16, 1190]}

    init_checking_functions = [closed_morris, morrises_number, blocked_number, pieces_number, two_piece_number,
                               three_piece_number]

    move_checking_functions = [closed_morris, morrises_number, blocked_number, pieces_number, opened_morris,
                               double_morris, winning_configuration]

    fly_checking_functions = [two_piece_number, three_piece_number, closed_morris, winning_configuration]

    evaluation = 0

    if mode == "INIT":
        init_coefs = phase_coefs["INIT"]
        for i in range(len(init_coefs)):
            evaluation += init_coefs[i]*init_checking_functions[i](board_state, player_color, last_played_move)

    elif mode == "MOVE":
        pass

    elif mode == "FLY":
        pass

    return evaluation


def closed_morris(board_state, player_color, last_played_move):
    closed_morris = 0

    if StateChecker().check_mill(board_state, last_played_move):
        if last_played_move.piece == player_color:
            closed_morris += 1
        else:
            closed_morris -= 1

    return closed_morris


def morrises_number(board_state, player_color, last_played_move):
    number_of_morrises = 0

    positions = [{"row": 0, "column": 1},
                 {"row": 1, "column": 1},
                 {"row": 2, "column": 1},
                 {"row": 3, "column": 0},
                 {"row": 3, "column": 1},
                 {"row": 3, "column": 2},
                 {"row": 4, "column": 0},
                 {"row": 4, "column": 1},
                 {"row": 4, "column": 2},
                 {"row": 5, "column": 1},
                 {"row": 6, "column": 1},
                 {"row": 7, "column": 1}]

    for position in positions:
        row = position["row"]
        column = position["column"]

        pos = board_state[row][column]

        if pos.piece == "o":
            continue

        elif StateChecker().check_mill(board_state, pos):

            if pos.piece == player_color:
                morris = 1
            else:
                morris = -1

            number_of_morrises += morris

    return number_of_morrises


def blocked_number(board_state, player_color, last_played_move):

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


def pieces_number(board_state, player_color, last_played_move):
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


def two_piece_number(board_state, player_color, last_played_move):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

    oponents_color = 'W' if player_color == 'B' else 'B'
    delta = 0

    for row in rows:
        for column in columns:
            position = board_state[row][column]
            for direction in position.next.keys():
                if position.has(direction):
                    next_pos = position.next[direction]
                    has_next = next_pos.has(direction)
                    found = False
                    while has_next:
                        found = position == next_pos
                        next_pos = next_pos.next[direction]
                        has_next = next_pos.has(direction)

                    if found:
                        if position.piece == player_color:
                            delta += 1
                        elif position.piece == oponents_color:
                            delta -= 1

    return delta



def three_piece_number(board_state, player_color, last_played_move):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))
    three = 0

    return three


def opened_morris(board_state, player_color, last_played_move):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))
    opened = 0

    return opened


def double_morris(board_state, player_color, last_played_move):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

    double = 0

    return double

def winning_configuration(board_state, player_color, last_played_move):
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




