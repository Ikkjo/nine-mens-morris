from interface.clear_screen import clear_screen
from interface.display_active_player import display_active_player
from interface.draw_gameboard import draw_gameboard
from scripts.change_active_player import change_active_player
from scripts.play_mill import play_mill
from repos.active_player import ActivePlayer
from repos.player_repo import PlayerRepo


def play(play_mode, finishing_condition):
    while finishing_condition():
        clear_screen()
        draw_gameboard()
        display_active_player()
        mill = play_mode()

        if mill and ActivePlayer().player.type == "human":
            play_mill()
        change_active_player()

    change_active_player()
    winner = ActivePlayer().player

    return winner
