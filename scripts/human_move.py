from services.player_service import PlayerService
from interface.move_menu import move_menu


def human_move():
    move = move_menu()
    PlayerService.move_piece(from_pos=move[0], to_pos=move[1])
    return move[1]