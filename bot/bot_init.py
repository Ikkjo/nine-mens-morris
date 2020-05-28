from services.player_service import PlayerService
from bot.best_move import best_move
from services.gameboard_service import GameboardService
from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo
from copy import deepcopy
from bot.bot_hardcoded import bot_random_place


def bot_init():

    players = PlayerRepo()
    if players.player1.pieces_left <= 1 and players.player2.pieces_left <= 1:  #  INIT Hardcoding
        position = bot_random_place()
    else:
        board_state = deepcopy(GameboardService().get_gameboard_state())
        player_color = None
        if ActivePlayer().player.type == "bot":
            player_color = ActivePlayer().piece_color
        position = best_move("INIT", board_state, player_color)

    row = position[0]
    column = position[1]
    PlayerService.place_piece(row, column)
    return position
