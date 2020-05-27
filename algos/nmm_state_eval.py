from services.gameboard_service import GameboardService
from repos.player_repo import PlayerRepo


def board_state_eval(node):
    board_state = node.data[0]
    player_color = node.data[1]
    mode = node.data[2]

    phase_coefs = {"INIT": [14, 37, 4, 14, 20, 2],
                  "MOVE": [16, 43, 11, 8, 7, 42, 1086],
                  "FLY": [10, 1, 16, 1190],
                  "MILL": []}

    init_checking_functions = [closed_morris, morrises_number, blocked_number, pieces_number, two_piece_number,
                               three_piece_number]

    move_checking_functions = [closed_morris, morrises_number, blocked_number, pieces_number, opened_morris,
                               double_morris, winning_configuration]

    fly_checking_functions = [two_piece_number, three_piece_number, closed_morris, winning_configuration]

    if mode == "INIT":
        init_coefs = phase_coefs["INIT"]
        evaluation = 0

        for i in range(init_coefs):
            evaluation += init_coefs[i]*init_checking_functions[i](board_state, player_color)

    elif mode == "MOVE":
        pass

    elif mode == "MILL":
        pass

    elif mode == "FLY":

    return evaluation


def closed_morris(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

    for row in rows:
        for column in columns:
            pass # Implement closed morris


def morrises_number(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def blocked_number(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def pieces_number(player_color):
    pass


def two_piece_number(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def three_piece_number(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def opened_morris(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def double_morris(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))

def winning_configuration(board_state, player_color):
    rows = range(len(board_state))
    columns = range(len(board_state[0]))





