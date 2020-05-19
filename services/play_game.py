from services.player_service import PlayerService, PlayerRepo
from services.gameboard_service import GameboardService
from services.choose_piece_color import choose_piece_color, second_player_piece_color


def play_game(mode: str):
    first_player_colour = choose_piece_color()

    if first_player_colour is None:
        return

    second_player_colour = second_player_piece_color(first_player_colour)

    player1 = PlayerService.new_player("human", first_player_colour)
    player2 = PlayerService.second_player(mode, second_player_colour)

    gameboard = GameboardService().gameboard

    initial_phase(player1, player2, gameboard)



