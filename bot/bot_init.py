from services.player_service import PlayerService
from bot.best_move import best_move
from services.gameboard_service import GameboardService
from repos.active_player import ActivePlayer
from copy import deepcopy


def bot_init():
    board_state = deepcopy(GameboardService().get_gameboard_state())
    player_color = None
    if ActivePlayer().player.type == "bot":
        player_color = ActivePlayer().piece_color
    position = best_move("INIT", board_state, player_color)
    row = position[0]
    column = position[1]
    PlayerService.place_piece(row, column)
    return position
