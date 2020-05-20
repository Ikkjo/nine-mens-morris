from services.player_service import PlayerService

def next_move(active_player, move_mode): # move_mode can be INIT, MILL or MOVE
    PlayerService.next_move(active_player, move_mode)

