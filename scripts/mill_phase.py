from repos.active_player import ActivePlayer
from services.player_service import PlayerService
from interface.mill_menu import mill_menu

def mill_phase():
    active_player = ActivePlayer().player
    position = get_mill_position(active_player.type)
    row = position[0]
    column = position[1]
    removed = PlayerService.mill_remove(row, column)


def get_mill_position(player_type):
    if player_type == "human":
        return get_human_mill_position()




def get_human_mill_position():
    return mill_menu()




