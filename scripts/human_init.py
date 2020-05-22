from interface.human_init_menu import init_menu
from services.player_service import PlayerService


def human_init():
    position = init_menu()
    row = position[0]
    column = position[1]
    PlayerService.place_piece(row, column)




