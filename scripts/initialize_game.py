from repos.player_repo import PlayerRepo
from services.choose_piece_color import choose_piece_color, second_player_piece_color
from services.gameboard_service import GameboardService
from services.player_service import PlayerService


def initialize_game(mode):
    GameboardService()
    make_players(mode)


def make_players(mode):
    first_player_colour = choose_piece_color()

    if first_player_colour is None:
        return False

    second_player_colour = second_player_piece_color(first_player_colour)

    player1 = PlayerService.new_player("human", first_player_colour)
    player2 = PlayerService.second_player(mode, second_player_colour)

    PlayerRepo(player1, player2)
