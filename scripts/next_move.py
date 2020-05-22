from services.player_service import PlayerService
from scripts.human_init import human_init

def next_move(active_player, move_mode): # move_mode can be INIT, MILL or MOVE
    move(active_player, move_mode)



def move(active_player, move_mode):
    if move_mode == "INIT":
        init_place(active_player)

    if move_mode == "MOVE":
        move_piece(active_player)

def make_move():
    pass

def init_place(active_player):
    if active_player.type == "human":
        human_init()

    if active_player.type == "bot":
        return # TODO: bot_init()

def move_piece(active_player):
    if active_player.type == "human":
        return  # TODO: human_move()

    if active_player.type == "bot":
        return  # TODO: bot_move()
    pass

def bot_init():
    pass

