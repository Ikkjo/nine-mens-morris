from services.new_player import PlayerService, PlayerRepo
from services.choose_piece_color import choose_piece_color


def play_game(mode: str):
    piece = choose_piece_color()

    if piece is None:
        return

    PlayerService.new_player()
