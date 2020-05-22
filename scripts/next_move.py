from services.player_service import PlayerService
from scripts.human_init import human_init

def next_move(active_player, move_mode): # move_mode can be INIT, MILL or MOVE
    move = get_move(active_player, move_mode)
    make_move(move)


def get_move(active_player, move_mode):
    if move_mode == "INIT":
        return init_place(active_player)

    if move_mode == "MOVE":
        return move_piece(active_player)

def make_move():
    pass

def init_place(active_player):
    if active_player.type == "human":
        return human_init()

    if active_player.type == "bot":
        return bot_init()

def move_piece(active_player):
    if active_player.type == "human":
        return human_move()

    if active_player.type == "bot":
        return bot_move()
    pass

def bot_init():
    pass

